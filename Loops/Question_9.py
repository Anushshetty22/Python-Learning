'''
Loops — Question 9 (Fibonacci Sequence)

❓ Problem:
Take an integer n and print:
👉 The first n terms of the Fibonacci sequence

📌 Fibonacci rule
Each number is the sum of the previous two:
0 1 1 2 3 5 8 13 21 ...

Because:
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
...
📌 Example
Input:
7
Output:
0 1 1 2 3 5 8

⚠️ Rules:
Use a loop
Don’t hardcode values
Handle edge cases:
n <= 0 → "Invalid input"

🧠 What this tests:
Multiple variables changing together
Sequential thinking
Loop updates
'''

#Answer-

n = int(input("Enter the number: "))

if n <= 0:
    print("Invalid input")
else:
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num