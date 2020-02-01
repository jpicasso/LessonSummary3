student_list = []

def create_student():
    name = input("Please enter the new student's name: ")
    student_data = {'name':name, 'marks': []}
    return student_data

def add_mark(student, mark):
    student['marks'].append(mark)
    return None

def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0
    total = sum(student['marks'])
    return total / number

def print_student_details(student):
    print("{}'s average mark is: {}" .format(student['name'], calculate_average_mark(student)))

def print_student_list(students):
    for i, student in enumerate(students):
        print('ID: {}' .format(i))
        print_student_details(student)

#menu apps allow you to interact with the user and runs all of the functions in the program
def menu():
    selection = input ('Enter "p" to print student list, "s" to add student, "a" to add a mark, q" to quit: ')
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input('Enter the student ID to add a mark to: '))
            student = student_list[student_id]
            new_mark = int(input('Enter the new mark to be added: '))
            add_mark(student, new_mark)
        selection = input ('Enter "p" to print student list, "s" to add student, "a" to add a mark, "q" to quit: ')

menu()
