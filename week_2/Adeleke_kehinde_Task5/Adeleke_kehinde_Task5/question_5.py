#5
#Modify Tuple
#Ask a user to enter three items for their shopping list.
print("Enter three items for shooping list: ")
list_items = input("Enter first item: "), input("Enter second item: "),input("Enter third item: ")
#Store in a tuple shopping_list
shopping_list = tuple(list_items)
#Convert it to a list, then ask for two more items to add.
lst = list(shopping_list)
lst.append(input("Enter item: "))
lst.append(input("Enter another item: "))
#Convert back to a tuple and print the updated list using join() to display items separated by " | ".
lst_2 = tuple(lst)
f_list = "|".join(lst_2)
print(f_list)