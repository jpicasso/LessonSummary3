# Exercise 7.

# Write a Python program which iterates the integers from 1 to 100. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

i = 1
string = ''
while i <= 100:
  if i % 5 == 0 and i % 3 == 0:
    string = string + "FizzBuzz,"
  elif i % 5 == 0:
    string = string + "Buzz,"
  elif i % 3 == 0:
    string = string + "Fizz,"
  else:
    string = string + str(i) + ","
  i=i+1
print(string)

