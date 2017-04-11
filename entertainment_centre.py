import fresh_tomatoes
import media

buffalo_66 = media.Movie("Buffalo 66", 
	"An ex-con and a girl", 
	"https://upload.wikimedia.org/wikipedia/en/b/b9/Buffalo_sixty_six_ver1.jpg", 
	"https://www.youtube.com/watch?v=1duitd-N1Us")

breathless = media.Movie("Breathless",
	"An American girl in Paris in the 60s",
	"https://upload.wikimedia.org/wikipedia/en/3/3f/%C3%80_bout_de_souffle_%28movie_poster%29.jpg",
	"https://www.youtube.com/watch?v=WCDEAu4R8hA")

goodfellas = media.Movie("GoodFellas",
	"A life in the mob",
	"https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
	"https://www.youtube.com/watch?v=2ilzidi_J8Q")

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

movies = [buffalo_66, breathless, goodfellas, dirty_rotten_scoundrels, uncle_buck, indiana_jones]

fresh_tomatoes.open_movies_page(movies)
