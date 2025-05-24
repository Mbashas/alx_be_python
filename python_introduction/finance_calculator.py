# Prompt user to input their monthly income

month_income = int(input("Enter your monthly income: "))
month_expense = int(input("Enter your total montly expenses: "))

# Declaring variables 

annual_interest = 0.05

# Calculating monthly saving

month_saving= month_income - month_expense
 
# Calculating projected saving after a year with annual interest 

projected_savings= month_saving * 12 + (month_saving * 12 * annual_interest)

# Printing the saving, monthly income and after interest savings

print(f"Your monthly savings are ${month_saving}")

print(f"Projected savings after one year, with interest, is: ${projected_savings}")

