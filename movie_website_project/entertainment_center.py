import media
import fresh_tomatoes

batman_begins = media.Movie("Batman Begins",\
"After training with his mentor, Batman begins his \
fight to free crime-ridden Gotham City from the\
corruption that Scarecrow and the League of Shadows have cast upon it.",\
"https://images-na.ssl-images-amazon.com/images/M/MV5BNTM3OTc0MzM2OV5BMl5BanBnXkFtZTYwNzUwMTI3._V1_.jpg",\
"https://www.youtube.com/watch?v=vak9ZLfhGnQ", "Chris Nolan","June 15th, 2005" )

the_dark_knight = media.Movie("The Dark Knight",\
"When the menace knownas the Joker \
emerges from his mysterious past, \
he wreaks havoc and chaos on the people of Gotham,\
the Dark Knight must accept one of the greatestpsychological and physical tests of his ability to fight injustice.",\
"http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg",\
"https://www.youtube.com/watch?v=kmJLuwP3MbY",\
"Chris Nolan", "July 18th, 2008")

the_dark_knight_rises = media.Movie("The Dark Knight Rises",\
"Eight years after the Joker's reign of anarchy,\
the Dark Knight, with the help of the enigmatic Catwoman,\
is forced from his exile to save Gotham City, \
now on the edge of total annihilation, \
from the brutal guerrilla terrorist Bane.",\
"http://www.movie-check.at/wp-content/uploads/2013/07/the-dark-knight-rises-new-batman-movie-poster.jpg",\
"https://www.youtube.com/watch?v=ay-Xg1oTeAs",\
"Chris Nolan", "July 20th, 2012")

man_of_steel = media.Movie("Man of Steel",\
"Clark Kent, one of the last of an \
extinguished race disguised as an unremarkable human,\
is forced to reveal his identity when Earth is invaded \
by an army of survivors who threaten to bring \
the planet to the brink of destruction.",\
"https://upload.wikimedia.org/wikipedia/en/thumb/8/85/ManofSteelFinalPoster.jpg/220px-ManofSteelFinalPoster.jpg",\
"https://youtu.be/sCQUrbdddOo",\
"Zack Snyder", "June 14th, 2013")

batman_v_superman = media.Movie("Batman v Superman: Dawn of Justice",\
"Fearing that the actions of Superman are left unchecked,\
Batman takes on the Man of Steel, \
while the world wrestles with what kind of a hero it really needs.",\
"https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",\
"https://youtu.be/fis-9Zqu2Ro",
"Zack Snyder", "March 25th, 2016")

wonder_woman = media.Movie("Wonder Woman",\
"Before she was Wonder Woman, she was Diana, princess of the Amazons,\
trained warrior. When a pilot crashes and tells of conflict in the outside world,\
she leaves home to fight a war, discovering her full powers and true destiny.",\
"https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg","https://www.youtube.com/watch?v=1Q8fG0TtVAY",\
"Patty Jenkins", "June 2nd, 2017")

justice_league = media.Movie("Justice League",\
"Fueled by his restored faith in humanity \
and inspired by Superman's selfless act, \
Bruce Wayne enlists the help of his newfound ally, \
Diana Prince, to face an even greater enemy.",\
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjI2NjI2MDQ0NV5BMl5BanBnXkFtZTgwMTc1MjAwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",\
"https://www.youtube.com/watch?v=3cxixDgHUYw",\
"Zack Snyder/Joss Whedon", "November 17th, 2017")

movies = [batman_begins,the_dark_knight, the_dark_knight_rises, \
         man_of_steel, batman_v_superman, wonder_woman,\
         justice_league]
fresh_tomatoes.open_movies_page(movies)
