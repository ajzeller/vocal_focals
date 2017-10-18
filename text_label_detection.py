"""
 VOCALFOCALS

 This application uses the Google Cloud Vision API on the Raspberry Pi with
 the Raspberry Pi Camera to recognize text from images and identify an object
 in the image with a label.

 More information can be found at vocalfocals.com

"""

import argparse
import base64
import picamera
import json
import subprocess
import time
import subprocess
from gtts import gTTS
import os
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# capture photo and name with timestamp

def takephoto():
    camera = picamera.PiCamera()
    camera.resolution = (1600, 1200) # sets camera resolution to 1600 x 1200 px
    timestr = time.strftime("%m-%d-%Y_%H-%M-%S")
    img_filename = 'vf_capture_' + timestr + '.jpg'
    camera.capture(img_filename)
    return img_filename

def main():

    img_name_to_parse = takephoto() # First take a picture
    print("image captured...")
    """Run a label request on a single image"""

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)

    with open(img_name_to_parse, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [
                    {
                        'type': 'TEXT_DETECTION',
                        'maxResults': 500
                    },
                    {
                        'type': 'LABEL_DETECTION',
                        'maxResults': 1
                    }
                ]
            }]
        })

        response = service_request.execute()
        print("response received...")

        # parse the text annotations from the image and remove newlines
        if 'fullTextAnnotation' in response["responses"][0]:
            image_text = 'I found the following text: ' + \
            response["responses"][0]["fullTextAnnotation"]["text"].\
            replace('\n',' ')

        else:
            image_text = "Sorry, I couldn't find any text."

        # Parse the most likely object label and add intro phrase
        if 'labelAnnotations' in response["responses"][0]:
            image_label = 'This object is most likely ' + \
            response["responses"][0]["labelAnnotations"][0]["description"] + '.'

        # create new .txt file with same name as image capture
        output_filename = img_name_to_parse.rsplit( ".", 1 )[ 0 ] + \
          '.txt'

        # open .txt file
        text_file = open(output_filename,'w')

        output_str = image_text + "\n" + image_label

        # write the final output text to .txt file for debugging and close
        text_file.write(output_str)
        text_file.close()

        print(output_str)

        # create object for Google Text-to-speech audio output
        # language=English, slow audio speed
        audio_output = gTTS(text=output_str, lang='en', slow=False)

        # name audio output file with same timestamp as captured image
        audio_output_file = img_name_to_parse.rsplit( ".", 1 )[ 0 ] + '.mp3'

        # save audio output file
        audio_output.save(audio_output_file)

        # playback audio file with mpg321
        os.system("mpg321 " + audio_output_file)

if __name__ == '__main__':

    main()
