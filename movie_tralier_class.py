import webbrowser

class Movie():
    def __init__(self, title, movie_storyline,poster_image_url, trailer_youtube):
        
        self.title=title
        
        self.movie_storyline=movie_storyline
        
        self.poster_image_url=poster_image_url
        
        self.trailer_youtube_url=trailer_youtube
        


    def show_tralier(self):
        webbrowser.open(self.trailer_youtube_url)
        
