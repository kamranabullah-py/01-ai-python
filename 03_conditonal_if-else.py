# Conditional if-elif-else 
print("===== STUDENT GRADE CALCULATOR =====")
name = input("Enter your name: ")
marks = float(input("Enter your marks (0-100): "))
if marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Congratulations ! Your grade is A+")
elif marks >= 80:
    print("Well done ! Your grade is A")
elif marks >= 70:
    print("Good job ! Your grade is B")
elif marks >= 60:
    print(", your grade is C")
elif marks >= 50:
    print(", your grade is D")
else:
    print(", you have failed. Better luck next time!")

