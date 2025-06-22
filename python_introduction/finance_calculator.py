# Prompt user to input their monthly income

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total montly expenses: "))

# Declaring variables 

annual_interest = 0.05

# Calculating monthly saving

monthly_savings = monthly_income - monthly_expenses
 
# Calculating projected saving after a year with annual interest 

projected_savings= monthly_savings * 12 + (monthly_savings * 12 * annual_interest)

# Printing the saving, monthly income and after interest savings

print(f"Your monthly savings are ${monthly_savings}")

print(f"Projected savings after one year, with interest, is: ${projected_savings}")

