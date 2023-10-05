import strings

#WORK VARIABLES for Hamming Distance
dna1 = 'GAGCCTACTAACGGGAT'
dna2 = 'CATCGTAATGACGGCCT'

#WORK VARIABLES for DNA complement
dna3 = 'AAAACCCGGT'

"""
1-Hamming Distance
2-Dna Complement
3-Exit
The program runs until the user chooses option 3.

Option 1 prompt the user for a string, call the get_hamming_distance function and display the result.
Option 2 prompt the user for a string, call the get_dna_complement function and display the result.
"""


"""
print(strings.get_hamming_distance(dna1, dna2))

print(strings.get_dna_complement(dna1))
"""

exit_clause = '3'
confirmation = 'YES'
user_selection = '0'

while user_selection != exit_clause:
    user_selection = input(' ' + "\x1B[4m" + 'Welcome to the Homework 5 Menu:' + "\x1B[0m" + '\n  Press [1] for Hamming Distance\n        [2] for Dna Complement\n        [3] to  Exit the program\n\t>>> ')
    if user_selection == '1':
        print(' Your Hamming Distance for:\n ' + dna1 + ' and\n ' + dna2 + ' is:', strings.get_hamming_distance(dna1, dna2))
        user_selection = strings.exit_confirmation_loop(user_selection)
    elif user_selection == '2':
        print(' Your DNA Complement for:\n ' + dna3 + '\tis\n', strings.get_dna_complement(dna3))
        user_selection = strings.exit_confirmation_loop(user_selection)
    elif user_selection == '3':  
        user_selection = strings.exit_confirmation_loop(user_selection)
    else: 
        print(' I apologize. That was an invalid entry.')
        user_selection = strings.exit_confirmation_loop(user_selection)




