"""
If-Else — Question 1 (Basic but important)

❓ Problem:
Take an integer input from the user and check:
👉 If the number is positive, print:
Positive number
👉 If the number is negative, print:
Negative number
👉 If the number is zero, print:
Zero

⚠️ Rules:
Use if, elif, else
Don’t hardcode values
Take input using input()
Convert input to integer

🧠 Think before coding:
What condition checks positive?
What about zero?
What remains for negative? """


#Answer-

num = int(input('Enter the number: '))

if num > 0 :
    print("Positive number")
elif num == 0 :
    print("Zero")
else :
    print("Negative Number")

