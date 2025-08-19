#1
# Explain each output of the program below.
num1 = int(input("Enter first number: ")) #Enter a first number
num2 = int(input("Enter second number: ")) #Enter second number
print(f"{num1} == {num2} : {num1 == num2}") #check if num1 is equal to num2 and answer is either true or false
print(f"{num1} != {num2} : {num1 != num2}") #check if num1 is not equal to num2 and answer is either true or false
print(f"{num1} > {num2} : {num1 > num2}") #check if num1 is greater than num2 and answer is either true or false
print(f"{num1} < {num2} : {num1 < num2}") #check if num1 is less thn num2 and answer is either true or false

# give 3 usercases or cenarios where you can apply the program below
# 1 Age comparison
# 2 price comparison
# 3 gender comparison

#- Write the code for 1 of the 3 use cases.
age_1 = input("Enter age of the first person: ")
age_2 = input("Enter the age of the second person: ")
print(f"First person age = {age_1}, Second person age = {age_2}")
print(f"Are they of the same age: {age_1 == age_2}")
print(f"Is  the first person older than the second person: {age_1 > age_2}")
print(f"Is the fisrt person younger than the second person: {age_1 < age_2}")
