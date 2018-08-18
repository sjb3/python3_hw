# draw and fill the matrix to see what has to be the increment,

# ex1

# def arith (n):
#     i = 1
#     sum = 0
#     while i <= n:
#         sum = sum + (i)
#         i += 1
#     # return sum
#     print('Results is: ', sum)
#
# arith(4)
# ex 2
# def geoSeries(n):
#     i = 1
#     sum = 0

#     while i <= n:
#         sum = sum + (1/2**i)
#         i +=1
#     print(sum)

# geoSeries(1)

# testcase geo(3) = 0.875
# testcase geo(5) = 0.96875
# testcase geo(7) = 0.9922875
# ex 3
# def main():
#     speed = float(input('Enter the speed of the vehicle (as miles/hour): '))
#     time = int(input('Enter time travelled: '))

#     calc_distance(speed, time)

# def calc_distance(speed, time):
#     # speed = 0
#     # time = 0
#     if time == 0:
#         print('0')
#     print('Hour(s)', 'Distance Travelled')
#     print('=============================')

#     while time > 0:
#         distance =  speed * time
#         # new_distance = reversed(distance)
#         print(time,  'Travelled hour @: ', distance)

#         time -= 1
# if __name__ == '__main__':
#     main()

# ex4

# def calc_total():
#     runnning_total = 0

#     running total += earned_comm

def user_input(prompt):
    data = input(prompt)
    return data

def processOneEmp():
    name = user_input("What's your name? ")
    sales_amt = float(user_input("What's your our sales figure? "))
    comm_rate = float(user_input("How about commision rate? "))/100
    earned_comm = sales_amt * comm_rate
    return name, sales_amt, comm_rate, earned_comm

def main():
    name, sales_amt, comm_rate, earned_comm = processOneEmp()
    print('The earned commision total should be :', "earned ${:,.2f}".format(earned_comm))
    another_emp = input("Is there another employee? ")
    running_total = earned_comm

    while another_emp == 'Y' or another_emp == 'y':
        name, sales_amt, comm_rate, earned_comm = processOneEmp()
        print('The earned commision total should be :', "earned ${:,.2f}".format(earned_comm))
        another_emp = input("Is there another employee? ")
        # print(">>>>>>", running_total)
        running_total += earned_comm
        print(">>>>>>", running_total)

    if (another_emp == 'N' or another_emp == 'n'):
        print('The earned commision total should be :', "${:,.2f}".format(running_total))
    else:
        print('Please enter valid info.')

if __name__ == '__main__':
    main()
