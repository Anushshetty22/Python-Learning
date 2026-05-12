'''
Loops — Question 6 (Factorial)

❓ Problem:
Take an integer input n and print:
👉 Factorial of n

📌 Example:
Input: 5
Output: 120

Because:
5 × 4 × 3 × 2 × 1 = 120

More examples:
Input: 4
Output: 24
Input: 1
Output: 1

⚠️ Rules:
Use a loop
No math library
Handle invalid input:
If n < 0 → print "Invalid input"

🧠 What this tests:
Multiplication accumulator
Loop boundaries
Edge cases (0, 1, negatives)

'''

#Answer-

num = int(input("Enter the number: "))

if num < 0:
    print("Invalid input")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print("The factorial is:", factorial)