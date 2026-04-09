"""
Question 11 — Even or Odd Checker

📌 Task:
Ask user to enter a number
Check:
If number is even → print "Even number"
If number is odd → print "Odd number"

🎯 Example
Enter a number: 7
Odd number
Enter a number: 10
Even number

⚠️ Important Points
👉 Convert input to int
👉 Use modulus operator %

💡 Hint (if needed)
👉 Think:
number % 2
If remainder = 0 → even
Else → odd

🎯 What this tests
Type conversion
Basic logic
Introduction to conditions
"""

number = int(input("Enter a Number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")