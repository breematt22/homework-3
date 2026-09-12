# File: continuous_interest.py
# A program to calculate continuously compounded interest.

import math


def main():
    principal = float(input("Enter the initial investment amount: "))
    years = float(input("Enter the length of the investment in years: "))
    rate = float(input("Enter the annual interest rate as a decimal: "))

    final_amount = principal * math.exp(rate * years)

    print("The final investment amount is", final_amount)


main()