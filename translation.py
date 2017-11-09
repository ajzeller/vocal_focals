import requests
import os
import json
import pprint

api_key = os.environ["API_KEY"]

url = 'https://translation.googleapis.com/language/translate/v2'

text = 'My name is Andrew.'

payload = { 'target' : 'es',
            'key' : api_key,
            'q' : text }

translation = requests.post(url, data=payload)
translation = json.loads(translation.text)
output =  translation['data']['translations'][0]['translatedText']
output = 'This translates to ' + output

print output
print(json.dumps(translation))
