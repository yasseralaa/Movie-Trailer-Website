import webbrowser


class Movie(object):
    """this is the movie class"""

    # Movie class constructor
    def __init__(self, movie_title, movie_poster_url,
                 trailer_youtube_url, movie_rating):
        self.title = movie_title
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = movie_rating

    # shows movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
