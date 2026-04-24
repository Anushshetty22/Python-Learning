'''
If-Else — Question 2


❓ Problem:
Take an integer input from the user and check:
👉 If the number is divisible by 5, print:
Divisible by 5
👉 Otherwise, print:
Not divisible by 5

⚠️ Rules:
Use if-else
Take input using input()
Convert to integer
Use modulus operator %

🧠 Hint (light one)
👉 A number is divisible by 5 if:
number % 5 == 0

'''
# Answer-

num = int(input("Enter the Number: "))

if num % 5 == 0 :
    print("Divisible by 5")
else :
    print("Not divisible by 5")