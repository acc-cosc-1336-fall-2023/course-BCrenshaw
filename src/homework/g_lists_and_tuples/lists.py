import os

exit_clause = 'EXIT'
stop_clause = 'STOP'
new_clause = 'NEW'
empty_clause = 'EMPTY'
confirmation_clause = 'YES'

homework_number = 'homework 7'
homework_number = homework_number.upper()
main_menu_header_text = ' \x1B[4m' + '\tWELCOME TO THE ' + homework_number + ' MENU:\x1B[0m'
selection1_text = '\tPress [1]\tto ADD or UPDATE an item or adjust quantity'
selection2_text = '\tPress [2]\tto DELETE an item'
selection3_text = '\tPress [3]\tto PRINT current item list'
exit_choice_text = '\tType  [exit]\tto exit the program'
stop_choice_text = '\tType  [stop]\tto return to the menu' 
input_prompt = '\033[1m' + '\033[96m' + '\n\t >>> ' + '\033[0m'
unknown_entry = '\033[91m' + '\033[1m' + '\t>>>INVALID ENTRY<<<' + '\033[0m'
exit_confirmation_text = '\033[93m' + '\n\tDo you want to exit?\n\tEnter [YES]\tto exit\n\tEnter [NO]\tto return to the menu.' + '\033[0m'
exit_text = '\x1B[3m' + '\033[1m' + '\033[91m' + '\tEXITING THE ' + homework_number + ' MENU' + '\x1B[0m'

widgets = {}

"""
    >>> START FUNCTIONS FOR TEST CASE HOMEWORK
"""

def add_inventory(widget_name, quantity):
    global widgets
    quantity = int(quantity)
    if widget_name not in widgets:
        widgets[widget_name] = quantity
    else:
        widgets[widget_name] += quantity

def remove_inventory_widget(widget_name):
    global widgets
    if widget_name in widgets:
        del widgets[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'

def state_global_widget_dictionary():
    global widgets
    return widgets

"""
    >>> STOP FUNCTIONS FOR TEST CASE HOMEWORK
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

def is_stop_clause(str):
    str = str.upper()
    global stop_clause
    return str == stop_clause or str == stop_clause[0:1:1] or str == stop_clause[0:2:1] or str == stop_clause[0:3:1]

def main_menu():
    global exit_clause, confirmation_clause, main_menu_header_text, selection1_text, selection2_text, input_prompt, unknown_entry, selection3_text
    user_selection = '0'
    count = 0
    
    while user_selection != exit_clause:
        if count < 1:
            os.system('clear')
            count += 1

        print(main_menu_header_text)
        print(selection1_text)
        print(selection2_text)
        print(selection3_text)
        print(exit_choice_text)

        user_selection = input(input_prompt)
        
        if user_selection == '1':
            sub_menu1()
            os.system('clear')
        
        elif user_selection == '2':
            print('\tWhich item would you like to delete?\n')
            widget_name = input(input_prompt)
            if widget_name not in widgets:
                print('\tItem not in list\n')
            else:
                del widgets[widget_name]
        
        elif user_selection == '3':
            if len(widgets) < 1:
                print('\tCurrent item list is empty\n')
            else:
                print('\tNAME\tQUANTITY')
                for n in widgets:
                    print('\t' + n + '\t' + str(widgets[n]))
            print('')
             
        elif is_exit_clause(user_selection) == True:
            user_selection = exit_confirmation(user_selection)
            
        else:
            print(unknown_entry)

def sub_menu1():
    global stop_clause, stop_choice_text
    sub_menu_header_text = ' \x1B[4m' + '\tWELCOME TO THE ITEM MANAGEMENT SYSTEM:\x1B[0m'
    choice1_text = '\tType  [1]\tto enter a new item name or search for current item'
    user_selection = '0'
    count = 0
    
    while user_selection != stop_clause:
        if count < 1:
            os.system('clear')
            count += 1

        print(sub_menu_header_text)
        print(choice1_text)
        print(stop_choice_text)

        user_selection = input(input_prompt)
        
        if user_selection == '1':
            print('\tInput item name:')
            widget = str(input(input_prompt))
            if widget in widgets:
                print('\t' + widget + ' currently has the quantity of', widgets[widget])
                print('\tEnter an amount to adjust the quantity by:')
                quantity = input(input_prompt)
                add_inventory(widget, quantity)
            else:
                print('\t' + widget + ' is new. What is the quantity to enter?')
                quantity = input(input_prompt)
                add_inventory(widget, quantity)
        
             
        elif is_stop_clause(user_selection) == True:
            user_selection = stop_clause
            
        else:
            print(unknown_entry)