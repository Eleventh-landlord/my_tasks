#Ask for inputs
distance = float(input("Enter distance in km: "))
fare_per_km = float(input("Enter fare per km: "))

#Calculate total fare
total_fare = distance * fare_per_km

#Display result with two decimal places
print(f"Total fare: ₦{total_fare:.2f}")
