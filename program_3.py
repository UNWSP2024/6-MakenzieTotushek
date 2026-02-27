# Author: Makenzie Totushek
# Date: 2/27/26
# Title: Tax Rate

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

total_sales = float(input("Enter the total amount for sales: "))
def cTax():
    county_tax = total_sales * 0.025
    return county_tax
def sTax():
    state_tax = total_sales * 0.05
    return state_tax
total_tax = cTax() + sTax()
print(f'The total county tax is ${cTax():.2f}')
print(f'The total state tax is ${sTax():.2f}')
print(f'The total sales tax is ${total_tax:.2f}')