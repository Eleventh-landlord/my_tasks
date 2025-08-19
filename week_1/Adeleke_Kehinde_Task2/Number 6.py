# Ask for inputs
full_name = input("Enter customer's full name: ")
units = int(input("Enter units consumed (kWh): "))
cost_per_unit = float(input("Enter cost per unit (₦): "))

#Calculate total bill
total_bill = units * cost_per_unit

#Print receipt
print("\n----- Electricity Bill Receipt -----")
print(f"Customer Name:\t{full_name}")
print(f"Units Consumed:\t{units} kWh")
print(f"Cost per Unit:\t₦{cost_per_unit:.2f}")
print(f"Total Bill:\t₦{total_bill:,.2f}")
print("-------------------------------------")
