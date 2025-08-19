#Ask for inputs
amount_naira = float(input("Enter amount in Naira: "))
rate_usd = float(input("Enter exchange rate to USD: "))
rate_gbp = float(input("Enter exchange rate to GBP: "))

#Convert
amount_usd = amount_naira / rate_usd
amount_gbp = amount_naira / rate_gbp

#Display in table format
print("\n------ Currency Conversion ------")
print(f"{'Currency':<15}{'Amount':>20}")
print("-" * 35)
print(f"{'Naira (₦)':<15}{'₦' + format(amount_naira, ',.2f'):>20}")
print(f"{'US Dollar ($)':<15}{'$' + format(amount_usd, ',.2f'):>20}")
print(f"{'British Pound (£)':<15}{'£' + format(amount_gbp, ',.2f'):>20}")
print("-" * 35)
