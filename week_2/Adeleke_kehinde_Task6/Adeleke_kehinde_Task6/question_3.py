#3
#- Store all seat numbers (1 to 50) in a set.
seat_number = set(range(1,50))
#- Ask users to "book" a seat by entering the number.
booking = int(input("Enter a booking number: "))
#- Remove booked seats from the set.
seat_number.remove(booking)
#- Show remaining seats after each booking.
print(f"Available sits remaining: {seat_number}")
