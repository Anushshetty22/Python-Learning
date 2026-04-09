"""
Question 12 — Largest of Two Numbers

📌 Task:
Ask user to enter two numbers
Check:
Which number is greater
If both are equal → print "Both numbers are equal"

🎯 Example
Enter first number: 10
Enter second number: 20
20 is greater
Enter first number: 15
Enter second number: 15
Both numbers are equal

⚠️ Important Points
👉 Convert inputs to int or float
👉 Use if, elif, else

💡 Hint (if needed)
👉 Think:
if a > b
elif b > a
else → equal

🎯 What this tests
Multiple conditions
Comparison operators
Decision making
"""

number_1 = float(input("Enter the First Number:"))

number_2 = float(input("Enter the Second Number:"))

if number_1 > number_2 :
    print(f"{number_1} is greater")
elif number_2 > number_1 :
    print(f"{number_2} is greater")
else :
    print("Both numbers are equal")

