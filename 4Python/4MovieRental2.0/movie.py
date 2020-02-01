#this file defines the Movie class, its properties and methods
class Movie:
    #this is a special function that creates a new Movie object
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    #instead of returning the memory location of the movie object, this returns the movie object movie name
    def __repr__(self):
        return "<Movie {}>".format(self.name)

    # json method takes the currently selected object and turns it into JSON format
    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    #load json data as a movie object
    #this code allows you to pass a dictionary
    @classmethod
    def from_json(cls, json_data):  # {'genre': '...', 'name': '...', 'watched': True}
        return Movie(**json_data)
