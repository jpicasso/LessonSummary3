import random

#menu function runs all the functions in the program
def menu():
    user_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    
    #Calculate winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print('you matched {}. You won ${}!' .format(matched_numbers,100**len(matched_numbers)))

#gets the user lottery numbers
def get_player_numbers():
    number_csv = input("Enter your 6 numbers, seperated by commas, between 1 and 20: ")
    number_list = number_csv.split(',')
    integer_set = {int(number) for number in number_list}
    return integer_set

#generates 6 random numbers
def create_lottery_numbers():
    values = set()
    while len(values) <6:
        values.add(random.randint(1,20))
    return values

#call menu function
menu()
