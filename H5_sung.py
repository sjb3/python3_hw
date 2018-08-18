# H5_sung.py
# set var score for user input(12:42PM)

score = int(input('Please Enter the test scores: '))

def point_to_grade(score):
    """
        From the user's, input numeric value, conversion happens here

        Return:
        grade, that contains numeric value converted to letter
    """
    if score >= 800:
        grade = 'A'
    elif 700 <= score < 800:
        grade = 'B'
    elif 600 <= score < 700:
        grade = 'C'
    elif 500 <= score < 600:
        grade = 'D'
    else:
        grade = 'E'
    return grade

print(point_to_grade(score))
