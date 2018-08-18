# ingredient_adjuster.py

# Basic formula:
# for 48 cookies = 1.5c sugar + 1c butter + 2.75c flour
# hence, the ratio should be 48cookies = 1.5s + 1b + 2.75f
# measuring unit should be c for cup

# promt for input by user
cookies = int(input('Please enter your desired amount of cookies you wish to bake: '))

# ingredients we need for cookies
sugar_needed = round((1.50/48) * cookies, 1)
butter_needed = round((1.00/48) * cookies, 1)
flour_needed = round((2.75/48) * cookies, 1)

# output
print('To bake ', cookies, ' cookies; you will need ', sugar_needed, ' cup sugar, ', butter_needed, ' cup butter and ', flour_needed, ' cup flour')
