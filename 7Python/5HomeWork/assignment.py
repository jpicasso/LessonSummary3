# # Exercises.

# # Exercise 1.

# # Write a function that takes a list of numbers and iterates through each number on a list and counts all numbers that are equal to 1.

# # a_list = [1,3,55,1,9,4,56,2,1,8]

# a_list = [1,3,55,1,9,4,56,2,1,8]
# x = 0
# for a in a_list:
#   if a == 1:
#     x= x+1
# print("You have {} numbers eqaul to 1" .format(x))

# # Exercise 2.

# # Write a Python program that accepts a string and calculate the number of digits and letters. use: help() to learn how to use isalpha() and isdigit()

# user_input = input('type something in: ')
# digits = 0
# letters = 0
# for symbol in user_input:
#   if symbol.isalpha():
#     letters = letters +1 
#   elif symbol.isdigit():
#     digits = digits +1

# print("You have {} digits and {} letters in your input. " .format(digits,letters))

# # Exercise 3.

# # Lets try to print these words backwards:

# # python
# # star
# # green
# # yellow
# # Exercise 4.

# user_input_3 = input('Type word to reverse: ')
# output_3 = ""
# for i in user_input_3:
#   output_3 = i + output_3
# print(output_3)

# Create a Temperature converter, Celsius to Fahrenheit:
# 0 degrees Celsius is equal to 32 degrees Fahrenheit:
# 0 °C = 32 °F
# The temperature T in degrees Fahrenheit (°F) is equal to the temperature T in degrees Celsius (°C) times 9/5 plus 32:
# T(°F) = T(°C) × 9/5 + 32

# Example:
# Convert 20 degrees Celsius to degrees Fahrenheit:
# T(°F) = 20°C × 9/5 + 32 = 68 °F

# Add:
# if Fahrenheit is more than 90, print statement "a heat warning", if Fahrenheit is less than 30, print statement "a cold warning"
# user_input_4 = float(input('Enter temperature in Celsius: '))
# output_4 = user_input_4*1.8 + 32
# if output_4 >90:
#   print('A heat warning. Temp is {} Fahrenheit' .format(output_4))
# elif output_4 <30:
#   print('A cold warning. Temp is {} Fahrenheit' .format(output_4))
# else:
#   print('Temp is {} Fahrenheit' .format(output_4))
  
# Exercise 5.

# In this exercise you will create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.

# user_input_5 = input('enter a letter: ')
# if user_input_5 == 'a' or user_input_5 == 'e' or user_input_5 == 'i' or user_input_5 == 'o' or user_input_5 == 'u':
#   print('{} is a vowel' .format(user_input_5))
# elif user_input_5 == 'y':
#   print('{} is sometimes a vowel and sometimes a consonant' .format(user_input_5))
# else:
#   print('{} is a consonant' .format(user_input_5))


# Exercise 6.

# Write a Python program to construct the following pattern.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

#slow compiling solution

# i = 0
# while i < 5:
#   string = ''
#   x = 0
#   while x <=i:
#     string = string + '*'
#     x=x+1 
#   print(string)
#   i = i +1

# string = '****'
# while string != '':
#   print(string)
#   string = string[:-1]

# simple and fast compiling solution
# triangle = '*'
# for x in range(0,6,1):
#     print(x*"*")

# # for x in range(4,0,-1):
#     print(x*"*")

# Exercise 7.

# Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# i = 1
# string = ''
# while i <= 100:
#   if i % 5 == 0 and i % 3 == 0:
#     string = string + "FizzBuzz,"
#   elif i % 5 == 0:
#     string = string + "Buzz,"
#   elif i % 3 == 0:
#     string = string + "Fizz,"
#   else:
#     string = string + str(i) + ","
#   i=i+1
# print(string)

# Exercise 8.

# In this exercise you will create a program that displays a multiplication table that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10. Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10. It should also include labels down the left side consisting of the numbers 1 through 10. When completing this exercise you will probably find it helpful to be able to print out a value without moving down to the next line. This can be accomplished by added end="" as the last parameter to your print statement. For example, print("A") will display the letter A and then move down to the next line. The statementprint("A", end="")will display the letter A without moving down to the next line, causing the next print statement to display its result on the same line as the letter A.

#         1    2    3    4    5    6    7    8    9   10 
#    1    1    2    3    4    5    6    7    8    9   10 
#    2    2    4    6    8   10   12   14   16   18   20 
#    3    3    6    9   12   15   18   21   24   27   30 
#    4    4    8   12   16   20   24   28   32   36   40 
#    5    5   10   15   20   25   30   35   40   45   50 
#    6    6   12   18   24   30   36   42   48   54   60 
#    7    7   14   21   28   35   42   49   56   63   70 
#    8    8   16   24   32   40   48   56   64   72   80 
#    9    9   18   27   36   45   54   63   72   81   90 
#   10   10   20   30   40   50   60   70   80   90  100

#slow solution
# x = 1
# y = 0
# while y <=10:
#   if y == 0:
#     print('\t', end="")
#     while x <=10:
#       if x == 10:
#         print(x)
#       else:
#         print(str(x)+'\t', end="")
#       x = x +1
#   else:
#     print(str(y)+'\t',end ="")
#     while x <=10:
#       if x == 10:
#         print(x*y)
#       else: 
#         print (str(x*y) +'\t', end ="")
#       x = x+1
#   y = y+1
#   x = 1 

# fast and simple solution
# for i in range (1,11,1):
#     for j in range(1,11,1):
#         print('{:4}' .format(i*j),end='')
#     print()


# Exercise 9.

# A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words. Write a program that reads a string from the user and uses a loop to determines whether or not it is a palindrome. Display the result, including a meaningful output message.

# input_9 = input('Enter a word: ')
# reverse_9 = input_9[-1:-len(input_9)-1:-1]
# if input_9 == reverse_9:
#   print('{} equals {}. This is a palindromic word.' .format(input_9, reverse_9))
# else:
#   print('{} does not equal {}. This is not a palindromic word.' .format(input_9, reverse_9))

# Exercise 10.

# One of the first known examples of encryption was used by Julius Caesar. Caesar needed to provide written instructions to his generals, but he didn’t want his enemies to learn his plans if the message slipped into their hands. As result, he developed what later became known as the Caesar Cipher. The idea behind this cipher is simple (and as a result, it provides no protection against modern code breaking techniques). Each letter in the original message is shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc. The last three letters in the alphabet are wrapped around to the beginning: X becomes A, Y becomes B and Z becomes C. Non-letter characters are not modified by the cipher. Write a program that implements a Caesar cipher. 
# - Allow the user to supply the message and the shift amount, and then display the shifted message. 
# - Ensure that your program encodes both uppercase and lowercase letters. 
# - Your program should also support negative shift values so that it can be used both to encode messages and decode messages. 
# Hints: ord(), chr()
#  https://learncryptography.com/classical-encryption/caesar-cipher
# In [ ]:

# message = input('Type the message you want encoded in the Caeser Cipher: ')
# shift_amount = int(input('How many letters do you want to shift: '))
# output = ''
# for i in message:
#   if i.isalpha():
#     # a = 97
#     # A = 65
#     if ord(i)>96:
#       converted_letter = chr((ord(i)-96 + shift_amount) % 26+96)
#       output = output + converted_letter
#     else:
#       converted_letter = chr((ord(i)-64 + shift_amount) % 26+64)
#       output = output + converted_letter   
#   else:
#     output = output + i

# print(output)

#excercise 11

# alist = [1,2,3,4]

# banana = 0

# for number in alist:
#     counter = counter + number
# print(banana)


# blist = []
# for x in alist:
#     blist.append(x*10)
# print(blist)

# shopping_list = ['apples', 'oranges', 'bread']
# new_item = input('what else should i get? ')
# shopping_list.append(new_item)

# for x in shopping_list:
#     print('dont forget to buy ', x)
#     if x == 'beer':
#         print('are you old enough to buy beer?')
#     elif x == 'apples':
#         print ('you already bought apples')

# for i in range(1,11,2):
#     print(i)

##PIG latin algorithm
# ß


# Exercise - Sentence case sentences
# Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this exercise, you will write a function that capitalizes the appropriate characters in a string. 
# ---A lowercase “i” should be replaced with an uppercase “I” if it is both preceded and followed by a space. 
# ---The first character in the string should also be capitalized
# ----as well as the first non-space character after a “.”, “!” or “?”. 
# 
# For example, if the function is provided with the string “what time do i have to be there? what’s the address?” then it should return the string “What time do I have to be there? What’s the address?”. 
# ---Include a main program that reads a string from the user, capitalizes it using your function, and displays the result.

# input = input('Type in your string: ')
# output = ''
# for i in range(0,len(input),1):
#     if i == 0:
#         output = output + input[i].upper()
#     elif i == 1:
#         output = output + input[i]
#     elif input[i] == 'i' and input[i-1]== ' ' and input[i+1]== ' ':
#         output = output + input[i].upper()
#     elif input[i-2] in ['.','!','?']:
#         output = output + input[i].upper()
#     else:
#         output = output + input[i]
# print(output)

# Exercise 1.

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

# user_input = input('enter word or quit: ')
# ex1 = []

# while user_input != "quit":
#     if user_input not in ex1:
#         ex1.append(user_input)    
#     user_input = input('enter word or quit: ')

# print(ex1)    



# Exercise 2.

# Write a program that takes a series of numbers (ending in 0). If the current number isthe same as the previous number, it says ‘Same’; if the current number is greater thanthe previous one, it says ‘Up’, and if it’s less than the previous one, it says ‘Down’. Itmakes no response at all to the very first number. For example, its output for the list 9,9, 8, 5, 10, 10, 0, would be Same, Down, Down, Up, Same (comparing, in turn, 9 and 9,9 and 8, 8 and 5, 5 and 10, 10 and 10). You may assume there are at least two numbersin the input.

# Enter the first number: 9
# Enter the next number (0 to finish): 9
# Same
# Enter the next number (0 to finish): 8
# Down
# Enter the next number (0 to finish): 5
# Down
# Enter the next number (0 to finish): 10
# Up
# Enter the next number (0 to finish): 10
# Same
# Enter the next number (0 to finish): 0

# user_input = int(input('enter number: '))
# previous_number = 5

# while user_input <10 and user_input > 0:
#     if user_input > previous_number:
#         print('up')
#     elif user_input < previous_number:
#         print('down')
#     else:
#         print('same')
#     previous_number = user_input

#     user_input = int(input('enter number: '))




# Exercise 3.

# Many people do not use capital letters correctly, especially when typing on small devices like smart phones. In this exercise, you will write a function that capitalizes the appropriate characters in a string. A lowercase “i” should be replaced with an uppercase “I” if it is both preceded and followed by a space. The first character in the string should also be capitalized, as well as the first non-space character after a “.”, “!” or “?”. For example, if the function is provided with the string

# “what time do i have to be there? what’s the address?” 

# then it should return the string 

# “What time do I have to be there? What’s the address?”
# Include a main program that reads a string from the user, capitalizes it using your function, and displays the result.

# Exercise 4.

# The Sieve of Eratosthenes is a technique that was developed more than 2,000 years ago to easily find all of the prime numbers between 2 and some limit, say 100.

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# A description of the algorithm follows:

# Write down all of the numbers from 0 to the limit Cross out 0 and 1 because they are not prime
# Set p equal to 2
# While p is less than the limit do
# Cross out all multiples of p (but not p itself)
# Set p equal to the next number in the list that is not crossed out
# Report all of the numbers that have not been crossed out as prime
# The key to this algorithm is that it is relatively easy to cross out every nth number on a piece of paper. This is also an easy task for a computer—a for loop can simulate this behavior when a third parameter is provided to the range function. When a number is crossed out, we know that it is no longer prime, but it still occupies space on the piece of paper, and must still be considered when computing later prime numbers. As a result, you should not simulate crossing out a number by removing it from the list. Instead, you should simulate crossing out a number by replacing it with 0. Then, once the algorithm completes, all of the non-zero values in the list are prime.

# Create a Python program that uses this algorithm to display all of the prime numbers between 2 and a limit entered by the user. If you implement the algorithm correctly you should be able to display all of the prime numbers less than 1,000,000 in a few seconds.

# Exercise 5.

# Did you know our numeral system - the symbols we use to represent numbers are called Arabic numerals? Fun fact, because now it gets serious. You're going to be translating Arabic to Italian.

# Have the input form accept a number from the user. When the form is submitted, have the function to_roman take an integer as an argument and return a roman numerals string.

# For example:

# 60 >> LX  
# 78 >> LXXVIII  
# 99 >> XCIX  
# 3000 >>> MMM
# Look up Roman Numerals to get a complete list and jog your memory on its ancient conventions.

# https://en.wikipedia.org/wiki/Roman_numerals
# This is an easy challenge to code, but can be a difficult mental exercise. Don't overcomplicate it! Hints: divmod(a, b)

# In [ ]:


#writing files
# s = 'hello world'
# alist = [100,200,300,400,500]
# with open('myfile.txt', 'w') as my_file:
#     my_file.write(s)
#     for i in range(0,len(alist),1):
#         my_file.write("\n"+str(alist[i]))

# #convert text file into a list of words
# x = 0
# with open('article.txt', "r", encoding='utf8') as my_file:
#     list_of_words = my_file.read().lower().split()
#     for i in list_of_words:
#         if i == 'the':
#            x+=1

# print(x) 

