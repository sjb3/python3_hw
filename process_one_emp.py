# Sung Byun
# Process_One_Emp excercise 4

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
