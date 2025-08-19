#2
# Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
no_of_attendee = int(input("Enter number of people attending seminar: "))
people = set()
for i in range (no_of_attendee):
    name = input("Enter names: ")
    if name in people:
        print("error")
    else:
        people.add(name)
sorted_names = sorted(people)
print("\nList of Attendees: ")
for name in sorted_names:
    print(name)