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
    start_time = time.time() # begin timer

    img_name_to_parse = takephoto() # First take a picture

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
                        'maxResults': 100
                    }
                ]
            }]
        })

        response = service_request.execute()

        # parse the text annotations from the image
        image_text = response["responses"][0]["fullTextAnnotation"]["text"]

        # remove newlines from text annotations
        image_text = image_text.replace('\n',' ')

        # Add introduction phrase
        voice_output_text = 'I found the following text: ' + image_text

        # Parse the most likely object label and add intro phrase
        voice_output_labels = 'This object is most likely ' + \
          response["responses"][0]["labelAnnotations"][0]["description"] + '.'

        # create new .txt file with same name as image capture
        output_filename = img_name_to_parse.rsplit( ".", 1 )[ 0 ] +
          '.txt'

        # open .txt file
        text_file = open(output_filename,'w')

        # concat the image text and labels for final output audio narration
        output_str = voice_output_text + voice_output_labels

        # write the final output text to .txt file for debugging and close
        text_file.write(output_str)
        text_file.close()

        print(voice_output_text)
        print
        print(voice_output_labels)
        print

        finish_time = time.time() # stop timer

        elapsed = finish_time - start_time # calculate elapsed time

        elapsed = 'Elapsed time: ' + str(round(elapsed, 3)) + ' seconds.'

        print(elapsed)

        # create object for Google Text-to-speech audio output
        # language=English, slow audio speed
        audio_output = gTTS(text=output_str, lang='en', slow=True)

        # name audio output file with same timestamp as captured image
        audio_output_file = img_name_to_parse.rsplit( ".", 1 )[ 0 ] + '.mp3'

        # save audio output file
        audio_output.save(audio_output_file)

        # playback audio file with mpg321
        os.system("mpg321 " + audio_output_file)

if __name__ == '__main__':

    main()
