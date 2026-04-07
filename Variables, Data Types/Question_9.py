"""
Question 9 — Reverse Number
📌 Task:
Ask user to enter a number
Reverse the number

👉 Example:
Input: 1234
Output: 4321

⚠️ Challenge Twist
👉 You must:
Treat input as string for reversing
Then convert it back to integer

🎯 Output Example
Enter a number: 5678
Reversed number is: 8765
Type: <class 'int'>

🎯 What this tests
String slicing
Type conversion (int ↔ str)

Logical thinking
💡 Hint (if needed)
👉 Think:
How to reverse a string?
([::-1] might help)
"""

number = input("Enter a number: ")

reversed_number = number[::-1]

print("Reversed number is:", reversed_number)

reversed_number = int(reversed_number)

print("Type:", type(reversed_number))