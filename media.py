import webbrowser


class Movie():
    """"This class gives us a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, my_movietitle, my_moviestoryline, my_posterimage, my_traileryoutube):
        self.title = my_movietitle
        self.storyline = my_moviestoryline
        self.poster_image_url = my_posterimage
        self.trailer_youtube_url = my_traileryoutube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_picture(self):
        webbrowser.open(self.poster_image_url)
