'''
Loops — Question 5 (Count Digits)

❓ Problem:
Take an integer input and print:
👉 How many digits the number has

📌 Example:
Input: 12345
Output: 5
Input: 7
Output: 1
Input: 900
Output: 3

⚠️ Rules:
Use a loop
Don’t convert to string
Use math logic (// 10)

🧠 What this tests:
Reusing digit-removal logic
Counter pattern (count += 1)

⚠️ Edge case to think about
What should happen if input is:
0
(Think carefully.)

'''

#Answer-

num = int(input("Enter the number: "))

if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        count += 1
        num //= 10

print("The number of digits is:", count)