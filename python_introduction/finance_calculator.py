monthly_income = input("Enter your monthly income: ")
monthly_income = int(monthly_income)

monthly_expenses = input("Enter your total monthly expenses: ")
monthly_expenses = int(monthly_expenses)

monthly_savings = monthly_income - monthly_expenses
annual_interest_rate = 0.05

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)


print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")