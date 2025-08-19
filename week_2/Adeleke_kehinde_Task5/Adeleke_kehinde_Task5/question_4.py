#4
#Tuple Unpacking
Details = input("Enter first name: "),input("Enter your age: "),input("Enter your favorite color: "),input("Enter your home town: ")
profile = tuple(Details)
name, age, color, town = profile
print(f"\nFirst name: {name}\n\nAge: {age}\n\nFavorite color: {color}\n\nhome town: {town}")