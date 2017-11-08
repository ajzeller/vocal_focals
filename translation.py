import requests
import os

api_key = os.environ["API_KEY"]

url = 'https://translation.googleapis.com/language/translate/v2'

text = 'My name is Andrew.'

payload = { 'target' : 'es',
            'key' : api_key,
            'q' : text }

translation = requests.post(url, data=payload)
output = 'This translates to ' + translation["data"]["translations"]["translatedText"]

print output
print translation.text
print translation
