# File: house_affordability.py
# A program to calculate how much can be financed
# with a given monthly mortgage payment.

def main():
    payment = float(input("Enter the monthly payment you can afford: "))
    rate = float(input("Enter the annual interest rate as a decimal: "))
    periods = 12

    principal_15 = payment * (
        (1 - (1 + rate / periods) ** (-15 * periods))
        / (rate / periods)
    )

    principal_30 = payment * (
        (1 - (1 + rate / periods) ** (-30 * periods))
        / (rate / periods)
    )

    print("Amount you can finance with a 15-year mortgage:", principal_15)
    print("Amount you can finance with a 30-year mortgage:", principal_30)


main()