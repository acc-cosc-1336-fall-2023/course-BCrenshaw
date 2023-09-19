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