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