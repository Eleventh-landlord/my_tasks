
#5
# Ask the user for 3 student names.
student_names = input("Enter first name: "),input("Enter second name: "),input("Enter third name: ")
# For each student, ask for their score.
student_score = int(input("First student score: ")),int(input("Enter second student score: ")),int(input("Enter third student score: "))
#Store the results in two lists (one for names, one for scores).
names = list(student_names)
scores = list(student_score)
#Print a formatted output showing Name — Score, aligned neatly.
print(f"First Name: {names[0]} - Score: {scores[0]}\nSecond Name: {names[1]} - Score: {scores[1]}\nThird Name: {names[2]} - Score: {scores[2]}")