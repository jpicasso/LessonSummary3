#import the movie Class from the movie.py file
from movie import Movie

#this file defines the User class
class User:
    #special method to create new User Objects
    def __init__(self, name):
        self.name = name
        self.movies = []

    #special method to return User name when the Object is returned rather than memory location
    def __repr__(self):
        return "<User {}>".format(self.name)

    #add movie method
    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    #delete movie method
    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    #watched function returns a list of movie objects in a list but only include movies that have been watched
    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

    #set watched function, change the movie object property 'watched' to True
    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    #transform user object into JSON
    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    #load JSON file and make it a class method so that you can use it before the User object has been created
    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user
