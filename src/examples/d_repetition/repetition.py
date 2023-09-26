def test_config():
    return True

def display_numbers(num):
    cnt = 0

    while cnt < num : 
        print('cnt of ' + str(cnt) + ' is < ' + str(num) + ' running ' + str(cnt +1) + ' next')
        cnt = cnt + 1   
       
def sum_of_squares(num):
    sum = 0 
    cnt = 0
    while num > 0 and cnt <= num :
        sum = sum + (cnt * cnt)
        cnt = cnt + 1
    return sum

def prompt_user():
    keep_going = 'y'
    while keep_going == 'y' or keep_going == 'Y' or keep_going == 'yes' or keep_going == 'Yes' or keep_going == 'YES':
        keep_going = input('Loop again?')

def for_intro_loop():
    for num in [1,2,3,4,5]:
        print(num)

def for_intro_loop_string():
    for lang in ['C++', 'C#', 'Java', 'Python']:
        print(lang)

def for_sum_of_squares(num):
    sum = 0

    for val in range(1, num+1):
        sum = sum + val * val

    return sum

def get_sum(num):
    sum = 0
    cnt = 0

    while(cnt <= num):
        sum += cnt
        cnt += 1

    return sum

def get_sum_for(num):
    sum = 0
    
    for n in range(num):
        sum += n + 1

    return sum

def for_num_range_s_start_value(num1, num2):

    for n in range (num1, num2+1):
        print(n)

def for_num_range_w_step_value(num, num1, num2):

    for n in range(num, num1, num2):
        print(n)

def for_display_squares(num1, num2):
    for n in range(num1, num2):
        square = n ** 2
        print(n, '\t' , square) # '\t' = a tab spacing

def while_validate_user_input():
    min_num = 1
    max_num = 10
    lot_number = -1

    while lot_number != 'Exit' and lot_number != 'exit':
        lot_number = input('Enter lot number (' + str(min_num) + '-' + str(max_num) + ') or type Exit: ')

        if lot_number.isnumeric():
            lot_number = int(lot_number) 

            if lot_number >= min_num and lot_number <= max_num:
                print('Lot Number = ' + str(lot_number))

            else:
                print('Lot number ' + str(lot_number) + ' is not in range ' + str(min_num) + ' - ' + str(max_num))

        else:
            print('Lot number must be numeric')
    
def nested_while_loop(row, col):
    i = 0

    while i < row:
        print('i: ', i, 'outer loop-wait for inner loop')
        i += 1
        j = 0

        while j < col:
            print('j: ', j, '\t inner loop')
            j += 1

        print('inner loop complete')

def nested_for_loop(row, col):
    
    for i in range (row):
        print('i: ', i, ' outer loop')

        for j in range(col):
            print('j: ', j, ' inner loop')

        print('inner loop complete')

    print('outer loop complete')

def for_multiplication_tables(row, col):

    for i in range(1, row+1):

        for j in range (1, col+1):

            print(str(i*j).rjust(3), end = ' ')
        
        print(' ')

def while_multiplication_table(row, col):
    i = 0

    while i < row:
        j = 0

        while j < col:
            product = (i + 1) * (j + 1)
            print(str(product).rjust(3), end = ' ')
            
            j += 1
    
        i += 1
        print(' ')

       