# Working hour(s) for each day of the week for Suddeth

mo = 8
tu = 7
we = 8
th = 8
fr = 6

hr_wage_suddeth = 8

total_hr = mo + tu + we + th + fr
# print(total_hr)

total_wage_suddeth = total_hr * hr_wage_suddeth

print('Suddeth made $ %d for the week' %total_wage_suddeth)

## Bartol's goal for this week is $342
## how many more hours does she need to make up the discrepance?

mo, tu, we, th, fr = 7, 5, 6, 5, 5

hr_wage_bartok = 9
total_hr = mo + tu + we + th + fr
# print(total_hr)

total_wage_bartok = total_hr * hr_wage_bartok

deficit = 342 - total_wage_bartok

hr_convert = deficit / 9

print('Bartok needs to work extra %d hour(s)' %hr_convert )
