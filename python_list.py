# PYTHON LISTS
# Introduction to Python Lists
# A list in Python is a built-in data structure used to store multiple items in a single variable. Lists can contain different data types, such as integers, strings, floats, and Boolean values.
# Lists are:
# Ordered: Items maintain their position.
# Mutable: Items can be changed after creation.
# Allow duplicates: The same value can appear multiple times.
# Flexible: Can store different data types.
# Indexed: Elements can be accessed using their index, starting from 0.



numbers = [10, 20, 30, 40, 50] #Creating Lists
names = ["Ali", "Ahmed", "Kamran"]
mixed = [10, "Python", 20.5, True]
empty_list = []
print(numbers)
print(names)
print(mixed)

#Accessing List Elements (Indexing)
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])
#List Slicing
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:3])
print(numbers[2:5])
print(numbers[:4])
print(numbers[2:])
print(numbers[::-1])


#Updating List Elements(by indexing)
colors = ["Red", "Blue", "Green"]
colors[0] = "Black"
colors[1] = "White"
print(colors)

#Adding Elements(by values)
fruits = ["Apple", "Banana"]
fruits.append("Mango")
fruits.insert(1, "Orange")
fruits.extend(["Grapes", "Peach"])
print(fruits)

numbers = [10, 20, 30, 40, 50]
numbers.remove(20) #Removing Elements
numbers.pop()
del numbers[0]
print(numbers)


# Important List Methods
data = [10, 20, 30, 20, 40]
print(data.count(20))
print(data.index(30))
data.reverse()
print(data)
data.sort()
print(data)
new_data = data.copy()
print(new_data)
data.clear()
print(data)


subjects = ["Math", "Physics", "English"]
print(len(subjects))  # List Length

languages = ["Python", "Java", "C++"]
print("Python" in languages) #checking values in lists
print("JavaScript" not in languages)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2  #Concatenation of Lists
print(result)



numbers = [1, 2, 3]
result = numbers * 3

print(result)


# Nested Lists (2D Lists)
students = [
    ["Ali", 85],
    ["Ahmed", 90],
    ["Kamran", 95]
]

print(students[0])
print(students[1][0])
print(students[2][1])


# 13. List Unpacking
student = ["Kamran", 20, "Computer Science"]
name, age, field = student
print(name)
print(age)
print(field)

list1 = [10, 20, 30]
list2 = [10, 20, 30]
print(list1 == list2)  #List Comparison
print(list1 != list2)


marks = [75, 85, 90, 65, 95]
print(max(marks)) #Finding Maximum
print(min(marks)) #Minimum
print(sum(marks)) #get sumn


#List Comprehension
numbers = [1, 2, 3, 4, 5
squares = [x ** 2 for x in numbers]
print(squares)

#Conditional List Comprehension
numbers = [10, 15, 20, 25, 30]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


original = [10, 20, 30]
copied = original.copy()  #Copying Lists
print(original)
print(copied)


my_list = [1, 2, 3, 4]  #Clearing Lists
my_list.clear()
print(my_list)



information = [
    "Kamran",
    20,
    85.5,
    True,
    ["Python", "AI"]
]   #List with Different Data Types

print(information)

