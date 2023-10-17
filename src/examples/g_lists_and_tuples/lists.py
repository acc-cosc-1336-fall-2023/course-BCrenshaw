def test_config():
    return True

def get_list_total_while(list1):
    index = 0
    sum = 0
    
    while(index < len(list1)):
        sum += list1[index]
        index += 1

    return sum
        

def get_list_total_for(list1):
    sum = 0

    for i in range(0, len(list1)):
        sum += list1[i]

    return sum

def get_list_return_value(list1):
    print(list1)
    list[0] = 0

    return list1
