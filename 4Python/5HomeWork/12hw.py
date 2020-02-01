



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

user_input = int(input('enter number: '))
previous_number = 5

while user_input <10 and user_input > 0:
    if user_input > previous_number:
        print('up')
    elif user_input < previous_number:
        print('down')
    else:
        print('same')
    previous_number = user_input

    user_input = int(input('enter number: '))




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

