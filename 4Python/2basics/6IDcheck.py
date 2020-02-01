age = input('how old are you?')

if age.isdigit():
    age = int(age)
    if age >= 21:
        print('you are old enough')
    elif age >=0:
        print('you are not old enough')
    else:
        print('you do not have a valid id')
else:
    input('please enter a valid whole number')
