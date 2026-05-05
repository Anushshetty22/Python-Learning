'''
Question 10 — Number Classification (Ultimate)

❓ Problem:
Take an integer input and print exactly one of the following:

Positive Even
Positive Odd
Negative Even
Negative Odd
Zero

⚠️ Requirements:
Use if-elif-else
Handle zero separately

Combine:
Sign check (+ / -)
Even/odd check

⚠️ What this tests:
Condition ordering
Combining conditions
Avoiding redundant checks
'''

#Answer-

num = int(input("Enter the number: "))

if num == 0:
    print("Zero")
elif num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if num % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")