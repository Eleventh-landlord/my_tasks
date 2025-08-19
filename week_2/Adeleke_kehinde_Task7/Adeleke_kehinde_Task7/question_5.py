#5
# Store three names and their phone numbers in two separate tuples.
names = ("John", "Mary", "Alex")
numbers = ("12345", "67890", "54321")
# Create a dictionary from them using dict(zip(...))
contacts = dict(zip(names, numbers))
# Ask the user for a name
search_name = input("Enter the name you want to look up: ")
# Display the corresponding number (or error message)
phone_number = contacts.get(search_name, "Contact not found")
print(f"\t{search_name} : {phone_number}")
