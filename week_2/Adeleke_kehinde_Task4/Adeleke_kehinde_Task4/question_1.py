#1
# Ask the user to input their favorite quote.
fav_quote = str(input("Enter your favorite quote : "))
#Convert it to title case.
quote = (fav_quote.title())
#Print it with quotation marks using escape sequences.
print(f"\"{quote}\"")