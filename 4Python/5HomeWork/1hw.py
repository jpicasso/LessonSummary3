# # Exercise 1.

# # Write a function that takes a list of numbers and iterates through each number on a list and counts all numbers that are equal to 1.

# a_list = [1,3,55,1,9,4,56,2,1,8]

a_list = [1,3,55,1,9,4,56,2,1,8]
x = 0
for a in a_list:
  if a == 1:
    x= x+1
print("You have {} numbers eqaul to 1" .format(x))

