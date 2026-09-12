# File: monthly_deposit_goal.py
# A program to calculate the monthly deposit needed to reach a savings goal.

def main():
    goal = float(input("Enter the amount you want to have after two years: "))
    rate = float(input("Enter the annual interest rate as a decimal: "))
    periods = 12

    monthly_deposit = goal * (rate / periods) / ((1 + rate / periods) ** 24 - 1)

    print("The amount to deposit each month is", monthly_deposit)


main()