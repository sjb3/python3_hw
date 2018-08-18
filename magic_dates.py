
# month has to be 1 - 12
month = int(input('Enter a month: '))
# day 1-30/31
day = int(input('Enter a day: ') )
# year last two digits
year = int(input('Enter a year: '))


# if (month * day) == year:
#     print("That date is magic!")
# else:
#     "Sorry, that's justa regular date... not magic"

# Use ternery instead
month * day == year
results = print("MAGIC") if ((month*day)) == year else (print("no Magic"))
