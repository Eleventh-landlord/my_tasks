#2
#Tuple and input
#Ask the user for 5 best friends’ names.
print("enter 5 best friends name: ")
names = input("First namme: "),input("Second name: "),input("third name: "),input("Third name: "),input("Fourth name: "),input("Fifth name: ")
#Store them in a tuple friends.
friends = tuple(names)
# Print the tuple in reverse order.
print(friends[::-1])
