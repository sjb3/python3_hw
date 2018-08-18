# H3_justin.py;

# require 2 input's:
# have the user type in the two values when prompted
purchase = input('Enter the Purchase Price: ')
amount = input('Enter the Amount Tendered: ')

purchase_price = int(purchase)/100
amount_tendered = int(amount)/100

# from the input's, outputs are provided for the user in correct format
print('Purchse Price: ', '${:,.2f}'.format(purchase_price))
print('Amount Tendered: ', '${:,.2f}'.format(amount_tendered))

# computational processes
change = (amount_tendered - purchase_price)

dollar_only = int(change)
after_dollar = (change-dollar_only)

qtr_only = int(after_dollar/0.25)
after_qtr = (after_dollar % 0.25)

dime_only = int(after_qtr/0.1)
after_dime = (after_qtr % 0.1)

nickel_only = int(after_dime/0.05)
after_nickel = ((after_dime % 0.05) * 100)

# changes-output
# there should be three scenarios, and each condition will be taken care of in if-elif-else statement

if(amount_tendered > purchase_price):
    print('Your Change is: ', '${:,.2f}'.format(change))
    print(dollar_only, 'one-dollar bill(s)\n', qtr_only, 'quater(s)\n', dime_only, 'dime(s)\n', nickel_only, 'nickel(s)\n', after_nickel, 'penni(es)')
elif(amount_tendered == purchase_price):
    print('It\'e even!, No Changes')
else:
    print("Your Amount Tendered is lesser than Purchase Price: hence, we can't process this transaction, please re-enter the values")
