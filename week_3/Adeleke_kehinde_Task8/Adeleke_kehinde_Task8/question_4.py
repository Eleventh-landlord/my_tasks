#4
#- Create an empty dictionary called student.
student = {}
#- Ask the user to input their name and age, then store them in the dictionary.
student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
# Add a list of scores (e.g., [70, 85, 90]) to the dictionary.
student["score"] = [70,85,90]
#- Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".
avg_score = sum (student["score"]) / len(student["score"])
student["passed"] = avg_score >= 50
#- Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".
student["Teenager"] = 13 <= student["age"] <=19
print(f"Student Record: \nName: {student['name']}\nAge: {student['age']}\nScores: {student['score']}\nPassed: {student["passed"]}\nTeenager: {student['Teenager']} ")