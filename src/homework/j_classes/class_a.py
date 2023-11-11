import random as r, os, time

class Die:
    def __init__(self):
        self.__roll_value = 0

    def state_rolled_value(self):
        print('The rolled value is',self.__roll_value)
    
    def get_rolled_value(self):
        self.__roll_value = r.randrange(1, 6)
        return self.__roll_value

exit_clause = 'EXIT'
confirmation_clause = 'YES'
stop_clause = 'STOP'

homework_number = 'homework 9'
homework_number = homework_number.upper()
main_menu_header_text = ' \x1B[4m' + '\tWELCOME TO THE ' + homework_number + ' MENU:\x1B[0m'
selection1_text = '\tPress [1]\tto roll the dice and receive a random 1 to 6 numeric value!'
exit_choice_text = '\tType  [exit]\tto exit the program'
input_prompt = '\033[1m' + '\033[96m' + '\n\t >>> ' + '\033[0m'
unknown_entry = '\033[91m' + '\033[1m' + '\t>>>INVALID ENTRY<<<' + '\033[0m'
exit_confirmation_text = '\033[93m' + '\n\tDo you want to exit?\n\tEnter [YES]\tto exit\n\tEnter [NO]\tto return to the menu.' + '\033[0m'
exit_text = '\x1B[3m' + '\033[1m' + '\033[91m' + '\tEXITING THE ' + homework_number + ' MENU' + '\x1B[0m'

"""
    >>> START FUNCTIONS FOR MENU NAVIGATION 
"""

def is_confirmed_clause(str):
    str = str.upper()
    global confirmation_clause
    return str == confirmation_clause or str == confirmation_clause[0:1:1] or str == confirmation_clause[0:2:1]

def exit_confirmation(user_confirmation):
    global exit_clause, confirmation_clause, exit_confirmation_text

    print(exit_confirmation_text)

    user_confirmation = input(input_prompt).upper()

    if is_confirmed_clause(user_confirmation) == True:
        result = exit_clause
        print(exit_text)
    else: result = 0    
    return result

def is_exit_clause(str):
    str = str.upper()
    global exit_clause
    return str == exit_clause or str == exit_clause[0:1:1] or str == exit_clause[0:2:1] or str == exit_clause[0:3:1] 

def main_menu():

    global exit_clause, confirmation_clause, main_menu_header_text, selection1_text, input_prompt, unknown_entry
    user_selection = '0'
    count = 0
    
    while user_selection != exit_clause:
        if count < 1:
            os.system('clear')
            count += 1

        print(main_menu_header_text)
        print(selection1_text)
        print(exit_choice_text)

        user_selection = input(input_prompt)
        
        if user_selection == '1':
            run_repetitive_rolling(user_selection)
            os.system('clear')
                     
        elif is_exit_clause(user_selection) == True:
            user_selection = exit_confirmation(user_selection)
            
        else:
            print(unknown_entry)

def run_repetitive_rolling(user_selection):
    global stop_clause, input_prompt

    while user_selection != stop_clause:
        
        print('Your number is:',Die().get_rolled_value(),' type STOP to quit at any time.')
        user_selection = input(input_prompt)

        if 's' in user_selection or 'S' in user_selection:
            user_selection = stop_clause

        else: user_selection = 1

