#4
#Ask the user to enter 5 names (separated by spaces).
names = input("Enter 5 names seperated by spaces: ")
#convert all names to lowercase
l_names = names.lower()
#Sort the list alphabetically.
names_list = l_names.split()
sorted_list = sorted(names_list)
print(sorted_list)
#Display them one name per line.
for name in sorted_list:
 print(name)