# Introduction to While Loop in Python:
# A while loop in Python is used to execute a block of code repeatedly as long as a given condition remains True. It is useful when we want to repeat a task but do not know exactly how many times it needs to run

'''USES OF WHILE_LOOP:
Repeated Execution: Run the same code multiple times.
User Input: Take input repeatedly until a condition is met.
Counting: Print numbers in ascending or descending order.
Calculations: Calculate sums, factorials, and multiplication tables.
List Operations: Access, update, search, and modify list elements.
Games: Create guessing games and interactive programs.
Menu Programs: Keep displaying a menu until the user chooses to exit.'''

count = 1
while count <= 5:
    print(count)
    count += 1

number = 1
while number <= 10:  #  Initialization, Condition and Updation
    print(number)
    number = number + 1


number = 10
while number >= 1: #Reverse Counting
    print(number)
    number -= 1


# Infinite While Loop
# while True:    
#     print("Python Programming")


number = 1
while number <= 10:
    if number == 6: 
        break      #break is use to stop running loop
    print(number)
    number += 1

number = 0
while number < 10:
    number += 1

    if number == 5:
        continue      #Continue Statement

    print(number)


#Else With While Loop
number = 1
while number <= 5:
    print(number)
    number += 1
else:
    print("Loop Completed!")


#  While Loop With If-Else
number = 1
while number <= 10:

    if number % 2 == 0:
        print(number, "Even")

    else:
        print(number, "Odd")

    number += 1


#  Nested While Loop
row = 1
while row <= 3:

    column = 1

    while column <= 3:
        print("*", end=" ")
        column += 1

    print()
    row += 1



# Create and Access List Elements

numbers = [10, 20, 30, 40, 50]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1



# Update List Elements
numbers = [10, 20, 30, 40]

index = 0

while index < len(numbers):
    numbers[index] += 5
    index += 1
print(numbers)


