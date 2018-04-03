# importing so urls open
import webbrowser


# making the movie class, with functions that pertain to the movie elements
class Movie():
    def __init__(self, movie_title, poster_image, storyline, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube

    # method to show trailer from url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
