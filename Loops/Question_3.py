'''
Loops — Question 3 (Reverse a Number)

❓ Problem:
Take an integer input and print:
👉 The number in reverse

📌 Example:
Input: 1234
Output: 4321
Input: 507
Output: 705

⚠️ Rules:
Use a loop
Don’t convert to string
Use math logic only

🧠 What this tests:
Digit extraction
Building a new number
Loop control

'''

#Answer-

num = int(input("Enter the number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("The reversed number is:", reverse)