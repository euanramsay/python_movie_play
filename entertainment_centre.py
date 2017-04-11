import fresh_tomatoes
import media
import film_data

films = ["Buffalo 66", "GoodFellas", "Uncle Buck", "Annie Hall", "Indiana Jones and the Last Crusade", "Dazed and Confused"]

movies = film_data.create_movie_objects(films)

fresh_tomatoes.open_movies_page(movies)
