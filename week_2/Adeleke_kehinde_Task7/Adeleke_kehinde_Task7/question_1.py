#1
# Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.
student_biodata = {}
name = input("Enter name: ")
age = int(input("Enter age: "))
gender = input("Enter gender: ")
courses = input("Enter courses seperated by commas:")
#  - Courses should be stored as a list.
courses = [course.strip() for course in courses.split(",")]
#store in dictionary
student_biodata["name"] = name
student_biodata["age"] = age
student_biodata["gender"] = gender
student_biodata["courses"] = courses
# Display the bio-data neatly using escape sequences.
print("\n\tStudent Biodata")
print(f"\tName : {name}\n\tAge : {age}\n\tGender : {gender}\n\tCourse : {courses}")