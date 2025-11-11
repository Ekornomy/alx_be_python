monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings =float(monthly_income) - float(monthly_expenses)
Projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"{monthly_income} {monthly_expenses} Your monthly savings are ${monthly_savings}. Projected savings after one year, with interest, is: ${Projected_savings}")
