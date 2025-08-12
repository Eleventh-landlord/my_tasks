empty_list = []
print(empty_list)

empty_list2 = list()
print(empty_list2)

numbers = [1,2,3,4,5]
print(numbers)

logez = ["h,e,&,*,g,h,y"]
print(logez)

fruits = ['apple, mango, banana, strawberry']
print(fruits)

mixed_list = ["Apple",25,36,True,"&" ]
print(mixed_list)

chars = list("hello")
print(chars)

mixed_list = list("hello")
print(mixed_list)

numbers = [1,2,3,4]
list_numbers =list(numbers)
print(list_numbers)

numbers_range = list(range(29))
print(numbers_range)

squares = [x**2 for x in range(10)]
print(squares)

evens = [x for x in range(10) if x % 2 ==0]
print(evens)

odds = [x for x in range (20) if x % 2  == 1]
print(odds)

matrix = [[3,1], [2,3], [4,9]]
print(matrix)
print(matrix[0])
print(matrix[0][0])
print(matrix[2])

fruits = ["Apple", "Mango", "Orange", "Banana"]
print(fruits)
print(fruits[2])
print(fruits[0][3])

items = ['scissors', 'rice', 'beans', 'beans', 'mango']
print(items)
print(list(items))

#list are mutable 1.e they can be changed
numbers = [1,2,3,4]
numbers[2] = 20
print(numbers)

fruits = ["yam", "mango", "apple", "guava"]
fruits[0] = 'orange'
print(fruits)

#A list can be mixed with different data types
mixed = [10,"nigeria", 10, 3.14, "nigeria", True]
print(mixed)


list = [[3,4], ["yam","egg"]]
print(list)
print(list[0])
print(list[1])

fruits = ["Mango"]
fruits.append("Apple")
fruits.append("Orange")
fruits.append(1)
print(fruits)

numbers = [1,2,3]
numbers.append(5)
print(numbers)

list_1 = [1,2,3]
list_2 = [4,5,6]
result = list_1 + list_2
print(result)

num = ["orange"]
mult = num * 3
print(mult)

fruits = ["Orange", "apple", "Mango"]
print(fruits[0])
print(fruits[-1])

numbers = [10,12,13,14,15]
print(numbers[:3])
print(numbers[0:])
print(numbers[::2])
print(numbers[1:4])
print(numbers[0:4])

colors = ["red", "orange", "blue"]
print("red" in colors)
print("blue" not in colors)
 
items = [1,2,3,4,5,6,7,8]
print(len(items))

items = ["book", "Money", "Pencil", "Ruler"]
print(len(items))

numbers = [1,2,3,4,3,2,5,9]
print(min(numbers))
print(max(numbers))

foods = ["Yam", "Egg", "Rice"]
print(min(foods))
print(max(foods))
print(sum(foods))


numbers = [1,2,3,4,5,6]
print(sum(numbers))

