import request
import media

movie_objects = []

def create_movie_objects(films):
  for film in films:
    film_data = request.get_film_data(film)
    movie_object = media.Movie(film_data[0], film_data[1], film_data[2], film_data[3])
    movie_objects.append(movie_object)
  
  return movie_objects
