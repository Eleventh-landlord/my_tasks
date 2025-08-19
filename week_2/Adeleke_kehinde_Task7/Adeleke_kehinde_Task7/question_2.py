#2
#Create a program that stores items and their prices in a dictionary.
item_price = {}
# Items should come from a list.
items = ["Apple","Banana","Mango","Pawpaw","Pineapple","Gun"]
#Prices are entered by the user.
for item in items:
    item_price[item] = float(input(f"Enter price for {item} in $: "))
for item, price in item_price.items():
# Display all items and prices, 
    print(f"{item} : ${price}")
#then allow the user to update the price of an item.
item_choice = input("Enter item you want to update price: ")
if item_choice in item:
    item_price[item_choice] = float(input(f"Enter new price of {item} in $: "))
    print(f"Price updated to ${item_price}")
else:
    print("Item not found") 
