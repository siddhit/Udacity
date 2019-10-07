import webbrowser

class Movie():
    """
        This class providesa  way to store movie related information.
        Attributes:
        .title: string containing movie title
        .storyline: string containing movie storyline
        .poster_image_url: string containing URL of image file\
        of movie poster
        .triler_youtube_url: a string of the URL that\
        will be converted by the function show_trailer\
        to start a trailer video
        .director: string containing name of director
        .release date: string denoting release date of movie.     
    """
    #VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, director, release_date):
        """
        Init function containg all the attributes to be\
        included in instance of class
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.release_date = release_date

    def show_trailer(self):
        """
        function that wil play the trailer of the movie.\
        Input is string .trailer_youtube_url
        """
        webbrowser.open(self.trailer_youtube_url)
