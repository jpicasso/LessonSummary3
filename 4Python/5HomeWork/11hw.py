
# Exercise 11.

# Avoiding Duplicates In this exercise, you will create a program that reads words from the user until the user enters “quit”. After the user enters a blank “quit” your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were entered.

# For example, if user enters:
# banana 
# apple 
# banana
# banana
# apple 
# then your program should display: 
# banana
# apple

user_input = input('enter word or quit: ')
ex1 = []

while user_input != "quit":
    if user_input not in ex1:
        ex1.append(user_input)    
    user_input = input('enter word or quit: ')

print(ex1)    


