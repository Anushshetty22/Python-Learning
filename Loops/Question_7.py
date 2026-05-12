'''
Loops — Question 7 (Prime Number Check)
❓ Problem:

Take an integer input and check:
👉 If the number is prime, print:

Prime
👉 Otherwise, print:

Not prime
🧠 Reminder: What is a prime number?
A number that has exactly 2 factors:

Examples:
1 itself
2 ✅ prime
3 ✅ prime
4 ❌ (divisible by 2)
7 ✅ prime
9 ❌ (divisible by 3)

⚠️ Rules:
Use a loop
No shortcuts
Handle edge cases:
0, 1, negative numbers → Not prime

🧠 What this tests:
Loop checking
Early stopping
Logical thinking
'''

#Answer-

num = int(input("Enter the number: "))

if num < 2:
    print("Not prime")
else:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Prime")
    else:
        print("Not prime")   