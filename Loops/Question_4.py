'''
Loops — Question 4 (Palindrome Number)

❓ Problem:
Take an integer input and check:

👉 If the number reads the same forward and backward, print:
Palindrome

👉 Otherwise, print:
Not a palindrome

📌 Example:
Input: 121
Output: Palindrome
Input: 123
Output: Not a palindrome

⚠️ Rules:
Use a loop
Don’t convert to string
Use the reverse logic from Q3

🧠 What this tests:
Reusing previous logic
Comparing original vs computed value
Problem decomposition

'''

#Answer-

num = int(input("Enter the number: "))

copy = num
rev = 0

while num > 0:
    rev = rev * 10 + (num % 10)
    num //= 10

if rev == copy:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")