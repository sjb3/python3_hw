# 0815

# test score averages (p. 192)
# num_studs = int(input('How many students do you have in your class? '))
# num_test_scores = int(input('How many test scores per student? '))
#
# for student in range(num_studs):
#     total = 0.0
#
#     print('Student number: ', student +1)
#     print('****************************')
#
#     for test_num in range(num_test_scores):
#         print('Test number: ', test_num+1, end='')
#         score = float(input('-'))
#         total += score
#
#     avg = total/num_test_scores
#
#     print('The average for student numer', student +1, 'is:', avg)
#     print()

# Nested For loops
# Below creates matrix
# for i in range(3):
#     for j in range(5):
#         print( 'i= ', i, 'j= ', j, sep='|')
# ^|
# see the dif
#
# for i in range(3):
#     print('i= ', i, end=':')
#     for j in range(3):
#         print(j, end='')
#     print()

# for i in range(1, 10):
#     print('i= ', i, end=':')
#     for j in range(10):
#         print(i * j, end=' ')
#     print()

# for j in range(-7, 8):
#     print(j, end='')

# for i in range(8):
#     for j in range(-i, i+1):
#         print(abs(j), end='')
#     print()

# if we wanna make a pyramid
for i in range(8):
    print(' '*(7-i), end='')
    for j in range(-i, i+1):
        print(abs(j), end='')
    print()
