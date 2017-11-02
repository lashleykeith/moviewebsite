import fresh_tomatoes
import media

rogue_one = media.Movie("Rogue One:", """Jyn Erso leads the Rebel Alliance in a risky move
                        to steal the plans for the Death Star,
                        setting up the epic saga to follow.""",
                        """ http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/12/rogue-one-novelization.jpg""",  # NOQA
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

lasttrailer = media.Movie("Star Wars: The Last Jedi Trailer",
                          "Star Wars: The Last Jedi Trailer",
                          """https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_SY1000_CR0,0,675,1000_AL_.jpg""",  # NOQA
                          "https://www.youtube.com/watch?v=Q0CbN8sfihY")

justice_league = media.Movie("Justice League",
                             """Batman, Wonderwoman, Flash,
                             Aquaman and Cyborg team up""",
                             """https://i.ytimg.com/vi/LzKMuViLx58/maxresdefault.jpg""",  # NOQA
                             "https://www.youtube.com/watch?v=92eQgQ65WBQ")

bDragon = media.Movie("Birth of the Dragon",
                      """Set against the backdrop of 1960s San Francisco,
                      BIRTH OF THE DRAGON is a modern take on the classic
                      movies that Bruce Lee was known for.""",
                      """https://images-na.ssl-images-amazon.com/images/M/MV5BMzk3OTQ4MjY0OF5BMl5BanBnXkFtZTgwNzQ2MTcwMzI@._V1_SY1000_CR0,0,677,1000_AL_.jpg""",  # NOQA
                      "https://www.youtube.com/watch?v=tVxY2uVkQTo")

blackp = media.Movie("BLACK PANTHER",
                     """T'Challa, after the death of his father, the King of Wakanda,
                     returns home to the isolated, technologically advanced
                     African nation
                     to succeed to the throne and take his
                     rightful place as king. """,
                     """http://fanfest.com/wp-content/uploads/2017/10/black-panther1.jpg""",  # NOQA
                     "https://www.youtube.com/watch?v=vt9UZo32KMk&t=7s")

guardians2 = media.Movie("Guardians of the Galaxy 2",
                         """The Guardians must fight to keep their newfound family
                         together as they unravel the mystery of Peter Quill's
                         true parentage. """,
                         """https://arhsnewspaper.com/wp-content/uploads/2017/05/guardians-of-the-galaxy-2-poster.jpg""",  # NOQA
                         "https://www.youtube.com/watch?v=duGqrYw4usE")

stevejobs = media.Movie("Steve Jobs",
                        """Steve Jobs takes us behind the scenes of the digital
                        revolution, to paint a portrait of the man at its
                        epicenter. """,
                        """https://upload.wikimedia.org/wikipedia/en/thumb/a/aa/SteveJobsposter.jpg/220px-SteveJobsposter.jpg""",  # NOQA
                        "https://www.youtube.com/watch?v=duGqrYw4usE")

pirates = media.Movie("Pirates of Silicon Valley",
                      " History of Apple and Microsoft.",
                      """https://images-na.ssl-images-amazon.com/images/M/MV5BNDc2NTE0NzE4N15BMl5BanBnXkFtZTgwMDQ5MzgwMzE@._V1_.jpg""",  # NOQA
                      "https://www.youtube.com/watch?v=xZGVgSw4Pho")


movies = [rogue_one, lasttrailer, justice_league,
          bDragon, blackp, guardians2, stevejobs, pirates]
# This command will activate the html automatically for you.
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__module__)
print(media.Movie.__name__)
