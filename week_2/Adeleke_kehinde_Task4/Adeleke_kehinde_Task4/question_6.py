#6
#Ask the user to input a word.
word = input("Enter a word: ")
#- Print the length of the word
print(len(word))
#Check if it is all uppercase, all lowercase, or title case.
if word.isupper():
    print("the word is in upper case")
if word.islower():
    print("word is in lower case")
if word.istitle():
    print("word is in title case")
#- Reverse the word using slicing.
print(word[::-1])