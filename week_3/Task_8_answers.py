#1
# Explain each output of the program below.
num1 = int(input("Enter first number: ")) #Enter a first number
num2 = int(input("Enter second number: ")) #Enter second number
print(f"{num1} == {num2} : {num1 == num2}") #check if num1 is equal to num2 and answer is either true or false
print(f"{num1} != {num2} : {num1 != num2}") #check if num1 is not equal to num2 and answer is either true or false
print(f"{num1} > {num2} : {num1 > num2}") #check if num1 is greater than num2 and answer is either true or false
print(f"{num1} < {num2} : {num1 < num2}") #check if num1 is less thn num2 and answer is either true or false

give 3 usercases or cenarios where you can apply the program below
1 Age comparison
2 price comparison
3 gender comparison

#- Write the code for 1 of the 3 use cases.
age_1 = input("Enter age of the first person: ")
age_2 = input("Enter the age of the second person: ")
print(f"First person age = {age_1}, Second person age = {age_2}")
print(f"Are they of the same age: {age_1 == age_2}")
print(f"Is  the first person older than the second person: {age_1 > age_2}")
print(f"Is the fisrt person younger than the second person: {age_1 < age_2}")


#2
#- Federal Government Scholarship Key Eligibility Requirements
name = input("Enter name: ")
Nationality = input("Enter Nationaity: ").title()
Enrollment = input("Enter either Graduate or Undergraduate: ").title()
scholarship = input("Are you on any scholarship  'yes or no': ").title()
Academic = input("Do you have 5 distinctions in relevant subjects including maths and english in WAEC/WASSCE 'Yes or No': ").title()
 
eligibility = (Nationality == "Nigeria") and (Enrollment == "Undergraduate") and (scholarship == "No") and (Academic == "Yes")
print("      Eligibity Status    ")
print ("_____________________________-")
print(f" Candidate: {name}\n Nationality: {Nationality}\n Enrollment: {Enrollment}\n Other Scholarship: {scholarship}\n Academic Qualification: {Academic}\n\n Eligility Status: {eligibility}")

#3
#- Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
items = ["Gun","Knife","belt","Glass","Nikeslide"]
prices = [20000,12000,5000,15000,25000]
# Start with an empty cart total (cart_total = 0).
cart_total = 0
cart_items = items[0],items[1]
#- Use assignment operators (+=) to add the price of some items into cart_total.
cart_total += prices[0]
cart_total += prices[1]
# Print the list of items and the total price using an f-string like this:
print(f"Items: {cart_items}\nTotal price: \u20A6{cart_total}")

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

#5
#- Create a dictionary called store with items and their available quantities. Example:
store = {"Book": 10, "Pen": 20, "Bag": 5}
#Ask the user to input the item they want to buy (e.g., "Pen").
buy = input("Enter what you want to buy e.g Pen : ").title()
#- Ask the user to input the quantity they want to purchase.
quantity = int(input("Enter the quantity you want: "))
print(f"Before purchase :{store}")
# Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
store[buy] = store.get(buy,0)
store[buy] -= quantity
store[buy] = max(0,store[buy])
# Print the updated dictionary in this format:
print(f"After purchase :{store}")

#6
name = input("Enter name: ")
age = int(input("Enter age: "))
utme = int(input("Enter UTME score: "))
choice = input("What schoolm is your first choice: ").title()
olevel = int(input("How many credit pass in O'level sitting do you have: "))
post_utme = input("Did you take part in POST UTME: ").title()
department = int(input("Whats your total score: "))
eligibility = (age >= 16) and (utme >= 200) and (choice == "Unilag") and (olevel >= 5) and (post_utme == "Yes") and ( department >= 200)
print(eligibility)