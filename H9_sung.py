# H9_sung.py
# Loan Payment Plan: when the user type in the price for the computer
# this program will generate a table for monthly payment schedule until monthly due drops below monthly payment

def comp_finance_plan(price):
    ''' first off generate the basic template for the schedule,
        then from the given numbers(input), each variables will be calculated and printed,
        being assigned to variables as well
    '''
    print('\t\t|***************************************|\n\n')
    print('\t\t\tMONTHLY PAYMENT SCHEDULE\t\n\n')
    print('\t\t|***************************************|\n')

    print('Month\t', end='')
    print('Balance', '\t',end='')
    print('Interests', end='\t')
    print('Payment', end='\t')
    print('\t', 'New Balance','\t\t')
    print('======================================================================')

    down_payment = price * 0.1
    int_rate = 0.01 # per month

    balance = price - down_payment # initial balance to start off
    mo_payment = balance * 0.05

    curr_balance = balance
    interest_owed = curr_balance * int_rate
    new_balance = curr_balance - mo_payment + interest_owed
    i = 0

    if new_balance <= mo_payment:
        return new_balance
    else:
        while curr_balance > mo_payment:

            print(format(i+1, '2d'), end='')
            print('\t', "${:,.2f}".format(curr_balance), sep='', end='')
            print('\t\t',"${:,.2f}".format(interest_owed), sep='', end='')
            print('\t\t',"${:,.2f}".format(mo_payment), sep='', end='')
            print('\t\t', "${:,.2f}".format(new_balance))

            new_balance = new_balance - mo_payment + interest_owed
            curr_balance = new_balance + mo_payment - interest_owed

            i += 1
        return i #, new_balance+mo_payment, int_rate*(price-down_payment), mo_payment, new_balance

def main():
    ''' Simple main function that prompts the user and calls the function above to tablulate the payment schedule
        returning value will be only the i (of indexing) as tabluation will be taken care of inside the while loop
        using print function for each iteration
    '''
    user_input = float(input("Please enter your purchased price for the item: "))
    i = comp_finance_plan(user_input)

main()
