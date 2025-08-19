#3
#Tuple Operations
#Create a tuple of 5 Nigerian states entered by the user.
print("Enter 5 Nigerian states: ")
state = input("First state: "),input("Second state: "),input("Third state: "),input("Fourth state: "),input("Fifth state: ")
#Print the first state and last state
print(state[0])
print(state[4])
#Check if "Lagos" is in the tuple and print "Yes" or "No".
print("lagos" in state)
#Print the number of states entered.
print(len(state))
