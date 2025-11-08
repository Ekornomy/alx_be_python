import re

Monthly_income =int(input("Enter your monthly income:\n"))
Total_monthly_expenses = int(input("Enter your total monthly expenses:\n"))

monthly_savings=float(Monthly_income) - float(Total_monthly_expenses)
Projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"{Monthly_income}\n{Total_monthly_expenses}\nYour monthly savings are ${monthly_savings}.\nProjected savings after one year, with interest, is: ${Projected_savings}")
