entered_value = int(input("Please enter any values: "))

if entered_value > 0:
    print(entered_value, " is positive, EVEN") if(entered_value % 2 == 0 ) else print(entered_value, " is positive, ODD")
elif entered_value < 0:
    print(entered_value, " is negative, EVEN") if(entered_value % 2 == 0 ) else print(entered_value, " is negative, ODD")
else:
    print('ZERO value')
