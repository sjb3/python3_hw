# wt = pounds
# ht = inches
# msg = optimal/over/under

#18.5 - 25: optimal
#below 18.5: under
#over 25: over

wt = int(input("Enter your current Body Weight in pounds: "))
ht = int(input("Enter your current Body Height in inches: "))

bmi = wt * (703/ht**2)

print("Your BMI is: ", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi > 25:
    print("Overweight")
else:
    print("Optimal")
