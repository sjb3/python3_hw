# sales_tax.py

# prompt for input by user
purchase = float(input('Please enter the amount of purchase: '))

# tax rates
state_sales_tax = 0.04
county_sales_tax = 0.02

# cal for each parameters
tendered_state_sales_tax = purchase * state_sales_tax
tendered_county_sales_tax = purchase * county_sales_tax
final_price = purchase + tendered_county_sales_tax + tendered_state_sales_tax

# outputs
print('Amount of purchase: ', purchase)
print('State Sales Tax ', tendered_state_sales_tax)
print('County Sales tax: ', tendered_county_sales_tax)
print('The Total of the Sales should be ', final_price)
