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