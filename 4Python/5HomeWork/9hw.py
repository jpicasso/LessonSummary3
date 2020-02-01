
# Exercise 9.

# A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words. Write a program that reads a string from the user and uses a loop to determines whether or not it is a palindrome. Display the result, including a meaningful output message.

input_9 = input('Enter a word: ')
reverse_9 = input_9[-1:-len(input_9)-1:-1]
if input_9 == reverse_9:
  print('{} equals {}. This is a palindromic word.' .format(input_9, reverse_9))
else:
  print('{} does not equal {}. This is not a palindromic word.' .format(input_9, reverse_9))

