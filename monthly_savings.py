# File: monthly_savings.py
# A program to calculate the final balance after two years of monthly deposits.

def main():
    deposit = float(input("Enter the amount deposited each month: "))
    rate = float(input("Enter the annual interest rate as a decimal: "))
    periods = 12

    final_balance = deposit * (((1 + rate / periods) ** 24 - 1) / (rate / periods))

    print("The final balance after two years is", final_balance)


main()