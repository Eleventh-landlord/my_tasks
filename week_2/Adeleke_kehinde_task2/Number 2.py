# Ask for the price as a string
price_str = input("Enter the price of garri per paint in naira: ")

# Convert to float
price_float = float(price_str)

# Display price in naira and kobo
print(f"The price of garri per paint is ₦{price_float:.2f} (naira and kobo).")
