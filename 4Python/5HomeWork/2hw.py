# # Exercise 2.

# # Write a Python program that accepts a string and calculate the number of digits and letters. use: help() to learn how to use isalpha() and isdigit()

user_input = input('type something in: ')
digits = 0
letters = 0
for symbol in user_input:
  if symbol.isalpha():
    letters = letters +1 
  elif symbol.isdigit():
    digits = digits +1

print("You have {} digits and {} letters in your input. " .format(digits,letters))

