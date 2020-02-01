from database import Database
from user import User

Database.initialize(database='learning', user='postgres', password='1234', host='localhost')

#menu runs the program
def menu():
    user_input = input("Enter 'a' to add a user, 'p' to print a specific users, 'l' to print a list of all users, or 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            user_email = input("Enter user's email: ")
            user_first_name = input("Enter first name: ")
            user_last_name = input("Enter last name: ")
            #add new user as an object User. Note that the none is used to autoincrement
            new_user = User(user_email,user_first_name,user_last_name,None)
            print(new_user)
            new_user.save_to_db()
        
        elif user_input == 'p':
            user_email = input('Type the email address of the user: ')
            user_to_print = User.load_from_db_by_email(user_email)
            print(user_to_print)
            print(user_to_print.first_name)
            print(user_to_print.last_name)
        
        elif user_input == 'l':
            User.print_user_db()
        
        user_input = input("Enter 'a' to add a user, 'p' to print a specific users, 'l' to print a list of all users, or 'q' to quit: ")

#run the program
menu()

# my_user = User.load_from_db_by_email('jose@schoolofcode.me')
# second_user = User('tommy@gmail.com', 'tommy', 'Smith', None)

# second_user.save_to_db()

# print(my_user)
# print(my_user.last_name)