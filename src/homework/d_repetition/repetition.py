

def get_factorial(num):
    sum = 1

    for n in range(1, num + 1):
        sum *= n
    
    return sum

def sum_odd_numbers(num):
    sum = 0
    cnt = 0

    while cnt <= num:
        if cnt % 2 != 0:
            sum += cnt
            #print(cnt, ' with sum', sum) Check parts
            cnt += 1
        else:
            cnt += 1

    return sum

def factorial_while_loop():
    
    back_clause = 'BACK'
    min_numeric_selection = 1
    max_numeric_selection = 10
    user_selection = 0

    user_selection = input(' Please make a selection from ' + str(min_numeric_selection) + ' to ' + str(max_numeric_selection) + '. Alternatively, you can exit with BACK.  \n\t>>> ')
    
    while user_selection != back_clause:
        
        if (user_selection.strip('-')).isnumeric():
            user_selection = int(user_selection)
            if user_selection < min_numeric_selection or user_selection > max_numeric_selection:
                user_selection = input(' Please make a selection INSIDE the range ' + str(min_numeric_selection) + ' to ' + str(max_numeric_selection) + '. Alternatively, you can exit with BACK.  \n\t>>> ')
            else: 
                print(' Your result is: ' + str(get_factorial(user_selection)))
                user_selection = input(' Please make a selection from ' + str(min_numeric_selection) + ' to ' + str(max_numeric_selection) + '. Alternatively, you can exit with BACK.  \n\t>>> ')
        
        elif user_selection.upper() == back_clause:
            user_selection = user_selection.upper()
            print(' Closing factorial analysis.')
        
        else: user_selection = input(' Please enter a NUMERIC value from ' + str(min_numeric_selection) + ' to ' + str(max_numeric_selection) + '. Alternatively, you can exit with BACK.  \n\t>>> ')


def sum_odd_numbers_loop():
    
    back_clause = 'BACK'
    min_numeric_selection = 1
    max_numeric_selection = 100
    user_selection = 0

    user_selection = input(' Please make a selection from ' + str(min_numeric_selection) + ' to ' + str(max_numeric_selection) + '. Alternatively, you can exit with BACK.  \n\t>>> ')
    
    while user_selection != back_clause:
        
        if (user_selection.strip('-')).isnumeric():
            user_selection = int(user_selection)
            if user_selection < min_numeric_selection or user_selection > max_numeric_selection:
                user_selection = input(' Please make a selection INSIDE the range ' + str(min_numeric_selection) + ' to ' + str(max_numeric_selection) + '. Alternatively, you can exit with BACK.  \n\t>>> ')
            else: 
                print(' Your result is: ' + str(sum_odd_numbers(user_selection)))
                user_selection = input(' Please make a selection from ' + str(min_numeric_selection) + ' to ' + str(max_numeric_selection) + '. Alternatively, you can exit with BACK.  \n\t>>> ')
        
        elif user_selection.upper() == back_clause:
            user_selection = user_selection.upper()
            print(' Closing sum of odds analysis.')
        
        else: user_selection = input(' Please enter a NUMERIC value from ' + str(min_numeric_selection) + ' to ' + str(max_numeric_selection) + '. Alternatively, you can exit with BACK.  \n\t>>> ')

def exit_loop(prompt):
    exit_clause = 'EXIT'
    confirmation = 'YES'
    user_confirmation = '0'
    if prompt.upper() == exit_clause or prompt.upper() == exit_clause[0:1:1] or prompt.upper() == exit_clause[0:2:1] or prompt.upper() == exit_clause[0:3:1]:
        user_confirmation = input(' Are you sure you want to exit? Enter Yes, all other selections will return you to the menu.\n\t>>> ')
        if user_confirmation.upper() == confirmation or user_confirmation.upper() == confirmation[0:1:1] or user_confirmation.upper() == confirmation[0:2:1]:
            result = exit_clause
            print(' Exiting the Homework 3 Menu')
        else: result = '0'
    else: result = '0'
    return result

def basic_exit_loop(prompt):
    exit_clause = 'EXIT'
    confirmation = 'YES'
    user_confirmation = '0'
    if prompt.upper() == confirmation or prompt.upper() == confirmation[0:1:1] or prompt.upper() == confirmation[0:2:1]:
        user_confirmation = input(' Are you sure you want to exit? Enter Yes, all other selections will return you to the menu.\n\t>>> ')
        if user_confirmation.upper() == confirmation or user_confirmation.upper() == confirmation[0:1:1] or user_confirmation.upper() == confirmation[0:2:1]:
            result = exit_clause
            print(' Exiting the Homework 3 Menu')
        else: result = '0'
    else: result = '0'
    return result