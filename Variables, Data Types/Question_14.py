"""
Question 14 — Grade Calculator

📌 Task:
Ask user for marks (0–100)
Assign grade based on marks:
Marks	Grade
≥ 90	A
≥ 75	B
≥ 60	C
≥ 40	D
< 40	Fail

⚠️ Important Twist
👉 If marks are:
Less than 0 OR greater than 100
👉 Print: "Invalid marks"

🎯 Output Example
Enter marks: 85
Grade: B
Enter marks: 120
Invalid marks

⚠️ Important Points
👉 Use:
if / elif / else
Logical operators (and, or)

💡 Hint (if needed)
👉 First check:
marks < 0 or marks > 100
Then proceed to grading

🎯 What this tests
Multiple conditions
Logical operators
Order of conditions
Real-world validation
"""
#Answer-

marks = float(input("Enter marks: "))

if marks < 0 or marks > 100 :
    print("Invalid Marks")
elif marks >= 90 :
    print("Grade : A")
elif marks >= 75 :
    print("Grade : B")
elif marks >= 60 :
    print("Grade : C")
elif marks >= 40 :
    print("Grade : D")
else :
    print("Fail")