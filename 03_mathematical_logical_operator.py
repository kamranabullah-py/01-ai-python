# Python Mathematical and Logical Operators
# ==========================================
# 1. Arithmetic (mathematical) operators
# 2. Comparison (relational) operators
# 3. Logical operators
# 4. Assignment operators
# 5. Operator precedence

# 1. ARITHMETIC OPERATORS
# Arithmetic operators perform mathematical calculations.

a = 10
b = 3
print("\n1. ARITHMETIC OPERATORS")
print("Addition (+):", a + b)             
print("Subtraction (-):", a - b)          
print("Multiplication (*):", a * b)       
print("Division (/):", a / b)             # 3.333...
print("Floor division (//):", a // b)     # 3
print("Modulus (%):", a % b)              #1
print("Exponentiation (**):", a ** b)     


# 2. COMPARISON OPERATORS
# Comparison operators compare two values.
# Every comparison returns either True or False.
x = 8
y = 5
print("\n2. COMPARISON OPERATORS")
print("Equal to (==):", x == y)           
print("Not equal to (!=):", x != y)       
print("Greater than (>):", x > y)         
print("Less than (<):", x < y)            
print("Greater than or equal (>=):", x >= y)  # True
print("Less than or equal (<=):", x <= y)     # False

# 3. LOGICAL OPERATORS
# Logical operators combine or reverse conditions.
# and: True only when both conditions are True.
# or:  True when at least one condition is True.
# not: Reverses True to False, and False to True.
age = 20
has_id = True

print("\n3. LOGICAL OPERATORS")
print("AND:", age >= 18 and has_id)       # True
print("OR:", age >= 18 or has_id)         
print("NOT:", not has_id)                 # False


# 4. ASSIGNMENT OPERATORS
# Assignment operators store or update a variable's value.
number = 10
print("\n4. ASSIGNMENT OPERATORS")
print("Initial value:", number)
number += 5   # Same as: number = number + 5
print("After += 5:", number)
number -= 3   
print("After -= 3:", number)
number *= 2   
print("After *= 2:", number)
number /= 4   # Same as: number = number / 4
print("After /= 4:", number)
number = 10
number //= 3
print("After //= 3:", number)
number = 10
number %= 3
print("After %= 3:", number)
number = 2
number **= 3
print("After **= 3:", number)


# 5. OPERATOR PRECEDENCE
# Python follows an order when an expression has multiple operators.
# Parentheses are evaluated first, followed by exponentiation,
# multiplication/division, and addition/subtraction.
print("\n5. OPERATOR PRECEDENCE")
print("10 + 2 * 3 =", 10 + 2 * 3)         # 16
print("(10 + 2) * 3 =", (10 + 2) * 3)     # 36
print("2 ** 3 * 2 =", 2 ** 3 * 2)         # 16


