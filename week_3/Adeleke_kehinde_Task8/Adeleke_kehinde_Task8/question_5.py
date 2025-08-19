#5
#- Create a dictionary called store with items and their available quantities. Example:
store = {"Book": 10, "Pen": 20, "Bag": 5}
#Ask the user to input the item they want to buy (e.g., "Pen").
buy = input("Enter what you want to buy e.g Pen : ").title()
#- Ask the user to input the quantity they want to purchase.
quantity = int(input("Enter the quantity you want: "))
print(f"Before purchase :{store}")
# Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
store[buy] = store.get(buy,0)
store[buy] -= quantity
store[buy] = max(0,store[buy])
# Print the updated dictionary in this format:
print(f"After purchase :{store}")
