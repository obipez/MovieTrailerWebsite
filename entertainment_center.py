# importing files 
import fresh_tomatoes
import requests
import media


CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
language = 'http://api.themoviedb.org/3/movie/76341?api_key={key}&language=en'
videos = 'https://api.themoviedb.org/3/movie/76341/videos?api_key={key}&language=en'
KEY = 'key'


def _get_json(url):
    r = requests.get(url)
    return r.json()


config = _get_json(CONFIG_PATTERN.format(key=KEY))
languageInfo = _get_json(language.format(key=KEY))
videoContent = _get_json(videos.format(key=KEY))

# making the movie objects
mad_max = media.Movie(
    languageInfo["original_title"],
    languageInfo["overview"],
    'http://image.tmdb.org/t/p/original/' + languageInfo["poster_path"],
    'http://youtube.com/watch?v=' + videoContent['results'][0]['key'])

ex_machina = media.Movie("Ex Machina",
                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiC240uzb8DLWqD2Y-W6HMI9d36eHaD9Cn_SuWGh2rd04s1L4l",
                         "A young programmer has to evaluate the human qualities of a humanoid A.I.",
                         "https://www.youtube.com/watch?v=XYGzRB4Pnq8")

only_god_forgives = media.Movie("Only God Forgives", "http://www.impawards.com/2013/posters/only_god_forgives.jpg",
                                "A drug-smuggler's mom gets him to look into his brother's death.",
                                "https://www.youtube.com/watch?v=Q9ziAWl9AEA")

her = media.Movie("Her", "https://ia.media-imdb.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_.jpg",
                  "In a near future, a lonely writer develops an unlikely relationship with an operating system designed to meet his every need.",
                  "https://www.youtube.com/watch?v=WzV6mXIOVl4")

predestination = media.Movie("Predestination",
                             "https://alchetron.com/cdn/Predestination-film-images-2b8be194-094c-4f74-bca1-13c82b98518.jpg",
                             "A time cop chases a vicious criminal through time.",
                             "https://www.youtube.com/watch?v=-FcK_UiVV40")

pandorum = media.Movie("Pandorum", "https://www.movieposter.com/posters/archive/main/102/MPW-51258",
                       "Crew members on a spaceship wake up with no knowledge of their mission or their identities.",
                       "https://www.youtube.com/watch?v=PItZ-qr9jG8")

equilibrium = media.Movie("Equilibrium", "https://www.dvdsreleasedates.com/posters/800/E/Equilibrium-movie-poster.jpg",
                          "A man with guns begins to feel.",
                          "https://www.youtube.com/watch?v=raleKODYeg0")

primer = media.Movie("Primer",
                     "https://i.pinimg.com/736x/50/e4/36/50e436d45e6df69e35391a7931b8e49f--publication-design-time-travel.jpg",
                     "Two inventors create a time travel device and have to deal with the consequences of their actions.",
                     "https://www.youtube.com/watch?v=3nj5MMURCm8")

gattaca = media.Movie("Gattaca", "https://images-na.ssl-images-amazon.com/images/I/91B7YWMLi1L._SL1500_.jpg",
                      "A genetically inferior man assumes the identity of a superior one in order to pursue his lifelong dream.",
                      "https://www.youtube.com/watch?v=BpzVFdDeWyo")

contact = media.Movie("Contact",
                      "https://i.pinimg.com/736x/51/20/67/512067a78f1f3fb0e3e0af5103d52d7c--cinema-posters-movie-posters.jpg",
                      "Dr. Ellie Arroway finds extraterrestrial intelligence sending plans for a mysterious machine.",
                      "https://www.youtube.com/watch?v=d9C2cF3KvP8")

jurassic_world2 = media.Movie("Jurassic World: Fallen Kingdom",
                              "https://i.pinimg.com/originals/32/26/99/322699f120c17c2728457969b59af12c.jpg",
                              "Owen and Claire go to rescue the remaining dinosaurs from a volcano eruption.",
                              "https://www.youtube.com/watch?v=NooW_RbfdWI")


# initializing the movie objects created and calling the function to implement them
movies = [ex_machina, only_god_forgives, mad_max, jurassic_world2, contact, pandorum, gattaca, equilibrium, her, predestination]

fresh_tomatoes.open_movies_page(movies)