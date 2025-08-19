#3
#- Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
items = ["Gun","Knife","belt","Glass","Nikeslide"]
prices = [20000,12000,5000,15000,25000]
# Start with an empty cart total (cart_total = 0).
cart_total = 0
cart_items = items[0],items[1]
#- Use assignment operators (+=) to add the price of some items into cart_total.
cart_total += prices[0]
cart_total += prices[1]
# Print the list of items and the total price using an f-string like this:
print(f"Items: {cart_items}\nTotal price: \u20A6{cart_total}")