#Ask for inputs
school_name = input("Enter the school name: ")
tuition_fee = float(input("Enter tuition fee: "))
hostel_fee = float(input("Enter hostel fee: "))
feeding_fee = float(input("Enter feeding fee: "))

#Calculate total
total_fee = tuition_fee + hostel_fee + feeding_fee

#Print receipt
print("\n----- School Fees Receipt -----")
print(f"School Name: {school_name}")
print(f"Tuition Fee: ₦{tuition_fee:,.2f}")
print(f"Hostel Fee:  ₦{hostel_fee:,.2f}")
print(f"Feeding Fee: ₦{feeding_fee:,.2f}")
print(f"Total Fee:   ₦{total_fee:,.2f}")
print("--------------------------------")
