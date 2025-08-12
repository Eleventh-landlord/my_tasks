#Write a program to take a string input from the user and display it in uppercase.
name = input("Enter Your Name: ")
print(name.upper())

#Given the string "python", print its first and last characters.
word = "Python"
print(word[0])
print(word[-1])

#Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
name = str(input("Enter your name: "))
print(f"Hello, {name}!")

#Write a program to count the number of characters in a string without using len().
character = input("Enter a string to count characters: ")
count = 0
for char in character:
    count += 1
print("Number of characters:", count)

#Given "Hello World", replace "World" with "Python".
word = "Hello World"
print(word.replace("World","Python"))

#Check if a given string contains the substring "python" (case-insensitive).
word = "I love python"
print(word.__contains__('python'))

#Write a program to reverse a string without using slicing ([::-1]).
string_input = input("Enter a string to reverse: ")
reversed_str = ""
for char in string_input:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)


#Given a string with extra spaces, remove the leading and trailing spaces.
word = "      Python     "
print(word.strip())

#Ask the user to enter a sentence and print the number of vowels in it.



#Convert a string "1234" to an integer and multiply it by 2.
str = "1234"
int =int(str)
mult = int * 2
print("answer: ",mult)

#Given "apple,banana,orange", split the string into a list of fruits.
fruits = "apple,banana,orange"
print(fruits.split(","))

# Ask the user for a sentence and print each word on a new line.
sentence = input("Enter a sentence: ")
print(sentence.split())

#Replace all spaces in a string with underscores (_).
word = "      Nigeria      "
print(word.replace(" ","_"))

#Count how many times the letter "a" appears in "Banana".
word = "Banana"
count_a = word.lower().count("a")
print(f"The letter 'a' appears {count_a} times in '{word}'.")

#Check if a given string starts with "https://".
url = input("Enter a url: ")
print(url.startswith("https://"))