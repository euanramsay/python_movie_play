import fresh_tomatoes
import media
import film_data

# array of the titles of all films to be displayed, this can be edited
films = (
	["Buffalo 66", "GoodFellas", "Uncle Buck", "Annie Hall", 
	"Indiana Jones and the Last Crusade", "Dazed and Confused"]
	)

# movies is an array of instances of Movie based on titles in the array films
movies = film_data.create_movie_objects(films)

fresh_tomatoes.open_movies_page(movies)
