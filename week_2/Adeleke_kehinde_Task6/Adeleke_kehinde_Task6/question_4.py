#4
#get the number of people you want to register
num_people = int(input("Enter number of people ready to vote: ")) 
reg_name = set()
for i in range (num_people):
#Ask for voter names 
    name = input("Enter name of voters: ")
    if name in reg_name:
#- If a voter tries to register twice, display a warning.
        print("error")
    else:
        reg_name.add(name)
#After registration, display the total number of unique voters.
print(len(reg_name))