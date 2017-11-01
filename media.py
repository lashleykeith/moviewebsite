import webbrowser

class Movie():
	""" This class provides a way to store movie related information """
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, mymovietitle, mymoviestoryline, myposterimage, mytraileryoutube):
		self.title = mymovietitle
		self.storyline = mymoviestoryline
		self.poster_image_url = myposterimage
		self.trailer_youtube_url = mytraileryoutube
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	def show_picture(self):
		webbrowser.open(self.poster_image_url)