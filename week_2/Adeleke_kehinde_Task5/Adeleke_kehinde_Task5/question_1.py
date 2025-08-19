#1
# Ask the user to enter three favorite Nigerian dishes (one at a time)
favorite_dishes = input("Enter first favorite dish: "),input("Enter second favorite dish: "),input("Enter third favorite dish: ")
#Store them in a tuple called dishes.
dishes = tuple(favorite_dishes)
#Print the tuple in a single line, separating items with commas.
print(dishes)
# Use the \n escape sequence to print each dish on a new line
print(f"{favorite_dishes[0]}\n{favorite_dishes[1]}\n{favorite_dishes[2]}")