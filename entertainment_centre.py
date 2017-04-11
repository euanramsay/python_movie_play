import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that come to life", 
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
	"https://www.youtube.com/watch?v=vwyZH85NQC4")

# print(toy_story.storyline)

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"http://www.youtube.com/watch?v=-9ceBgWV8io")

# print (avatar.storyline)

# avatar.show_trailer()

goodfellas = media.Movie("Goodfellas",
	"A life in the mob",
	"https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
	"https://www.youtube.com/watch?v=2ilzidi_J8Q")

# goodfellas.show_trailer()

midnight_in_paris = media.Movie("Midnight in Paris",
	"Going back in time to meet authors",
	"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
	"https://www.youtube.com/watch?v=atLg2wQQxvU")

dirty_rotten_scoundrels = media.Movie("Dirty Rotten Scoundrels",
	"Two con men compete in the French Riviera",
	"https://upload.wikimedia.org/wikipedia/en/2/2c/Dirty_rotten_scoundrels_film.jpg",
	"https://www.youtube.com/watch?v=0ke-v0e3Cd4")

uncle_buck = media.Movie("Uncle Buck",
	"A crazy uncle babysits his nieces and nephew",
	"https://upload.wikimedia.org/wikipedia/en/8/8c/Uncle_buck.jpg",
	"https://www.youtube.com/watch?v=JQaeUz7K83w")

indiana_jones = media.Movie("Indiana Jones and the Last Crusade",
	"Indian Jones on an adventure with his dad",
	"https://upload.wikimedia.org/wikipedia/en/f/fc/Indiana_Jones_and_the_Last_Crusade_A.jpg",
	"https://www.youtube.com/watch?v=a6JB2suJYHM")

movies = [toy_story, avatar, goodfellas, midnight_in_paris, dirty_rotten_scoundrels, uncle_buck, indiana_jones]

fresh_tomatoes.open_movies_page(movies)
