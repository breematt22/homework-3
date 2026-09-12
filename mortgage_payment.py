# File: mortgage_payment.py
# A program to calculate the monthly payment for a mortgage.

def main():
    principal = float(input("Enter the amount to finance: "))
    years = int(input("Enter the term of the loan in years: "))
    rate = float(input("Enter the annual interest rate as a decimal: "))
    periods = 12

    monthly_payment = principal / (
        (1 - (1 + rate / periods) ** (-years * periods))
        / (rate / periods)
    )

    print("The monthly payment is", monthly_payment)


main()