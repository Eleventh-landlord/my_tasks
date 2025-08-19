#1. Welcome Screen
print("Welcome to Naija Mobile Service!")

#2. Ask for USSD code
ussd_code = input("Please dial a USSD code (e.g., *123#): ")

#3. Display menu
print("\nUSSD Menu:")
print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")

#4. Ask for user choice
choice = input("Enter your choice (1, 2, or 3): ")

#5. Confirmation message
if choice == "1":
    print(f"\nYou selected: Check Balance")
    print("Your account balance is ₦5,000.00")  # mock balance

elif choice == "2":
    print(f"\nYou selected: Buy Airtime")
    amount = float(input("Enter airtime amount (₦): "))
    print(f"You have successfully purchased ₦{amount:.2f} airtime.")

elif choice == "3":
    print(f"\nYou selected: Buy Data")
    amount = float(input("Enter data amount in GB: "))
    print(f"You have successfully purchased {amount:.2f}GB of data.")

else:
    print("\nInvalid option. Please try again.")

# 7. Thank you message
print("\nThank you for using Naija Mobile Service!")
