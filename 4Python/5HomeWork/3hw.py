# # Exercise 3.

# # Lets try to print these words backwards:

# # python
# # star
# # green
# # yellow


user_input = input('Type word to reverse: ')
output = ""
for i in user_input:
  output = i + output
print(output)