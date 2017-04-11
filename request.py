import json
import requests

title = "Uncle Buck"

r = requests.get('http://www.omdbapi.com/?t=' + title)

film_data = json.loads(r.text)

print film_data['Plot']