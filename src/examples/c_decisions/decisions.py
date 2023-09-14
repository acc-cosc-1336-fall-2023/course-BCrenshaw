def test_config():
    return True

def is_overtime(hours):
    result = False
    result = hours > 40
    return result

def get_letter_grade(grade):
    letter_grade = ""

    if (grade > 100 or grade < 0): letter_grade = "Invalid Grade"
    elif(grade >= 90 and grade <=100): letter_grade = "A"
    elif(grade >= 80 and grade <90): letter_grade = "B"
    elif(grade >= 70 and grade <80): letter_grade = "C"
    elif(grade >= 60 and grade <70): letter_grade = "D"
    else: letter_grade = "F"

    return letter_grade


def display_menu():
    print('1-Simple if')
    print('2-if else')
    print('3-if elif')

def run_menu():
    display_menu()
    option = input('Enter a menu option(1, 2, or 3): ')

    handle_menu_option(option)

def selected_option_2 ():
    print('User Selected Option 2')

def handle_menu_option(option):
    if(option == '1'): print('User Selected Option 1')
    elif(option == '2'): selected_option_2
    elif(option == '3'): print('User Selected Option 3')
    else: print('Invalid Option')
