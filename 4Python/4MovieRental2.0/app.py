#import json and os libraries so that you can use the methods in those libraries
import json
import os

#import the User class from the user.py file to use the User class
from user import User

#menu runs your program
def menu():
    #get users name; if the user file already exists, load that file, if it doesn't, create a new user
    name = input("Enter your name: ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    #give user options to add movies, see list of movies, set movie as watched, delete movies, see watched movies, save a text json file or quit
    user_input = input("Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies, 'f' to save or 'q' to quit: ")
    
    while user_input != 'q':
        #if a, use the user class add movie object to add a user
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
        
        #if s, pull up the user's movie list which is a list of movie objects and pull the movie properities from that list
        elif user_input == 's':
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
        
        #if w, use the user method, set_watched, to change the value to set watched
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        
        #if d, use the user method, delete_movie, to change delete the movie
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)

        #if l, cycle through the user list of watched movies (pulled up in the user method watched_movies) and print each movie object
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
        
        #if f, save user file as a new text file using JSON to pass the data through the text file
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        # keep giving the user options until they quit
        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies, 'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies, 'f' to save or 'q' to quit: ")

#check to see if the file exists
def file_exists(filename):
    return os.path.isfile(filename)

#run the program
menu()
