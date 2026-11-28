
#Introduction to For Loop in Python
#A for loop in Python is used to repeat a block of code for each item in a sequence, such as a list, tuple, string, or range.

for number in range(5):
    print(number)


for number in range(1, 6):  #Start and Stop
    print(number)


for number in range(2, 11, 2):      #Start, Stop, and Step
    print(number)

for number in range(10, 0, -1):  #Negative Step
    print(number)

for number in range(-5, 1):  #Range with Negative Numbers
    print(number)



numbers = list(range(1, 6)) #Convert Range into a List
print(numbers)


numbers = range(1, 11)
print(len(numbers))  # range Length



numbers = range(1, 11)    #Check Number in Range
print(5 in numbers)
print(15 in numbers)




numbers = range(10, 51, 10)
print(numbers[0])  #Access Range Elements Using Index
print(numbers[2])
print(numbers[-1])



numbers = range(1, 6)
print(sum(numbers))  #Sum of Range


numbers = range(1, 101)
print("Minimum:", min(numbers))  # Minimum
print("Maximum:", max(numbers))  #Maximum



