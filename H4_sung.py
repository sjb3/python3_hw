# H4_sung.py

# Below will prompt to fill out the package plan and service hours by users
# input
package_select = input('Please Enter Your Package Plan: ')
usage_hours = int(input('Please Enter Your Service Hours: '))

# Basically, if user type in wrong package plan(non-existent), I wanna display output and prompt back to the initial page,
# but don't know how to break away from the if - else chain, YET

# Calculate the monthly bills
# intial process for computation
# usage_hours_a: var used for Plan A less than 10 hrs, if it goes more than 10 hrs, use usage_hours_a_extra for cost justification
# same rules are applied for plan B
# for plan C, it's unifor price plan, hence no cost justification necessary

usage_hours_a = usage_hours * 9.95
usage_hours_a_extra = 10 * 9.95 + (usage_hours - 10) * 2
usage_hours_b = usage_hours * 13.95
usage_hours_b_extra = 20 * 13.95 + (usage_hours - 20) * 1
usage_hours_c = 19.95
# another Value checking for valid input and output's
if (package_select not in ('A', 'a', 'B', 'b', 'C', 'c')):
    print('Sorry, Your Input is not Valid, Please Re-enter Your Package Plan')
else:
    if package_select == 'A' or package_select == 'a':
        if usage_hours <= 10:
            print('Plan A: Your Service charge for the month is: ', '${:,.2f}'.format(usage_hours_a))
            if usage_hours_a > usage_hours_b:
                print('Suggestion: by switching to Plan B, you can save: ', '${:,.2f}'.format(usage_hours_a - usage_hours_b))
            if usage_hours_a > usage_hours_c:
                print('Suggestion: by switching to Plan C, you can save: ', '${:,.2f}'.format(usage_hours_a - usage_hours_c), '!')
        else:
            print('Plan A: Your Service charge for the month is: ', '${:,.2f}'.format(usage_hours_a_extra))
            if usage_hours_a_extra > usage_hours_b_extra:
                print('Suggestion: by switching to Plan B, you can save: ', '${:,.2f}'.format(usage_hours_a_extra - usage_hours_b_extra), '!')
            if usage_hours_a_extra > usage_hours_c:
                print('Suggestion: by switching to Plan C, you can save: ', '${:,.2f}'.format(usage_hours_a_extra - usage_hours_c), '!')
    elif package_select == 'B' or package_select == 'b':
        if usage_hours <= 20:
            print('Plan B: Your Service charge for the month is: ', '${:,.2f}'.format(usage_hours_b))
            if usage_hours_b > usage_hours_c:
                print('Suggestion: by switching to Plan C, you can save: ', '${:,.2f}'.format(usage_hours_b - usage_hours_c), '!')
        else:
            print('Plan B: Your Service charge for the month is: ', '${:,.2f}'.format(usage_hours_b_extra))
            if usage_hours_b_extra > usage_hours_c:
                print('Suggestion: by switching to Plan C, you can save: ', '${:,.2f}'.format(usage_hours_b_extra - usage_hours_c), '!')
    else:
        print('Plan C: Your Service charge for the month is: ', '${:,.2f}'.format(usage_hours_c))
