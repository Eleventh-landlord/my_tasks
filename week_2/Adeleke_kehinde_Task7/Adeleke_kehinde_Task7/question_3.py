#3
# Store days of the week in a tuple and ask the user to input an activity for three specific days.
weeks = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
week = input("Enter name of first day: "),input("Enter name of second day: "),input("Enter name of third day: ")
if week in weeks:
        print(week)
else:
        print("Wrong date included")
activity = input(f"Enter name of actvity for {week[0]}: "),input(f"Enter name of actvity for {week[1]}: "),input(f"Enter name of actvity for {week[2]}: ")
#- Use dictionary comprehension to pair days and activities.
paired_dict = {week: value for week,value in zip(week, activity)}
#Print the dictionary.
print(paired_dict)