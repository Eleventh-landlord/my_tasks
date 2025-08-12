#Ask for inputs
market_name = input("Enter the market name: ")
num_traders = int(input("Enter the number of traders: "))
daily_revenue = float(input("Enter the daily revenue in naira: "))

#Display result with comma as thousands separator
print(f"Market: {market_name}\nNumber of Traders: {num_traders:,}\nDaily Revenue: ₦{daily_revenue:,.2f}")
