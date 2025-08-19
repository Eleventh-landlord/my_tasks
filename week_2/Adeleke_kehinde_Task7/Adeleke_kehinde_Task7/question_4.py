#4
# Ask the user to enter three names separated by commas.
names = input("Enter three names separated by commas: ")
# Convert them to a set to ensure uniqueness.
set_of_names = set([name.strip() for name in names.split(",")])
# Create a dictionary where each name is a key and its length is the value.
name_length_dict = {name: len(name) for name in set_of_names}
# Print the dictionary
print(f"\t{name_length_dict}")