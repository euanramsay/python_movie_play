import json
import requests

def get_film_data(film_title):
	# sends request to OMDb API to get film data
	omdb_request = requests.get('http://www.omdbapi.com/?t=' + film_title)
	
	film_data = json.loads(omdb_request.text)

	title = film_data['Title']
	storyline = film_data['Plot']
	poster = film_data['Poster']

	# sends request to search YouTube API based on film title
	API_KEY = 'AIzaSyBUYgsqikPPzNpli9IrZbi1Ge9cfoaJ0IQ'

	youtube_request = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&key=' + API_KEY + '&q='+ film_title + ' trailer')

	trailer_data = json.loads(youtube_request.text)

	# creates full youtube url
	youtube_url = 'https://www.youtube.com/watch?v=' + trailer_data['items'][0]['id']['videoId']

	# puts all data for a single film in an array
	film_data = [title, storyline, poster, youtube_url]
	
	# returns array containing film data
	return film_data

