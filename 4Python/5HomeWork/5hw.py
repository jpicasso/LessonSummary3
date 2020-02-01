# Exercise 5.

# In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program 
# should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating 
# that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.

user_input = input('enter a letter: ')
if user_input == 'a' or user_input == 'e' or user_input == 'i' or user_input == 'o' or user_input == 'u':
  print('{} is a vowel' .format(user_input))
elif user_input == 'y':
  print('{} is sometimes a vowel and sometimes a consonant' .format(user_input))
else:
  print('{} is a consonant' .format(user_input))

