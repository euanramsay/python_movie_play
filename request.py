import json
import requests

def get_film_data(film_title):

	omdb_request = requests.get('http://www.omdbapi.com/?t=' + film_title)
	
	film_data = json.loads(omdb_request.text)

	title = film_data['Title']
	storyline = film_data['Plot']
	poster = film_data['Poster']


	API_KEY = 'AIzaSyBUYgsqikPPzNpli9IrZbi1Ge9cfoaJ0IQ'

	youtube_request = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&key=' + API_KEY + '&q='+ film_title + ' trailer')

	data = json.loads(youtube_request.text)

	youtube_url = 'https://www.youtube.com/watch?v=' + data['items'][0]['id']['videoId']

	film_data = [title, storyline, poster, youtube_url]

	return film_data

