'''
If-Else — Question 3

❓ Problem:
Take an integer input from the user and check:
👉 If the number is even, print:
Even number
👉 If the number is odd, print:
Odd number

⚠️ Rules:
Use if-else
Use % operator
Take input and convert to integer

🧠 Think before coding:
Even numbers → divisible by 2
Odd numbers → not divisible by 2

👉 Condition to check:
num % 2 == 0

⚠️ Common mistake to avoid:
Don’t overcomplicate with multiple conditions — this is a simple binary case.

'''

#Answer-

num = int(input("Enter the Number: "))

if num % 2 == 0 :
    print("Even Number")
else :
    print("Odd Number")