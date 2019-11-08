import random

magic_numbers = [random.randint(0,9),random.randint(0,9)]
chances = 3

def ask_user_and_check_number():
    user_number = int(input("enter a number between 0 and 9:"))
    if user_number in magic_numbers:
        print("you got it right")
    if user_number not in magic_numbers:
        print("you got it wrong")

def run_program_x_times():
    for attempt in range(chances):      #range(chances) is [0,1,2]
        print("this is attempt {}" .format(attempt+1))
        ask_user_and_check_number()

run_program_x_times()