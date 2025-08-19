#7
#- Create a list of five cities.
city = ["Lagos", "Surulere", "Lekki", "Mowe","Ikeja"]
#- Replace the third city with a new one (entered by the user).
new_city = input("Enter new city: ")
city[2] = new_city
#- Remove the last city.
city.remove("Ikeja")
#- Add a new city to the beginning of the list.
city.insert(0,"Ajah")
#- Print the updated list.
print(city)