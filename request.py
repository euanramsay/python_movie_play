import json
import requests

title = 'Buffalo 66'

omdb_request = requests.get('http://www.omdbapi.com/?t=' + title)

film_data = json.loads(omdb_request.text)

print 'Title: ' + film_data['Title']
print 'Storyline: ' + film_data['Plot']
print 'Poster: ' + film_data['Poster']


API_KEY = 'AIzaSyBUYgsqikPPzNpli9IrZbi1Ge9cfoaJ0IQ'

youtube_request = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&key=' + API_KEY + '&q='+ title + ' trailer')

data = json.loads(youtube_request.text)

print 'YouTube URL: https://www.youtube.com/watch?v=' + data['items'][0]['id']['videoId']

