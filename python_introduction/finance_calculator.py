Monthly_income = int(input("Enter your monthly income:"))
Total_monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = float(Monthly_income) - float(Total_monthly_expenses)
Projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"{Monthly_income} {Total_monthly_expenses} Your monthly savings are ${monthly_savings}. Projected savings after one year, with interest, is: ${Projected_savings}")
