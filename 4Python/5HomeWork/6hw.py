
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
triangle = '*'
for x in range(0,6,1):
    print(x*"*")

for x in range(4,0,-1):
    print(x*"*")

