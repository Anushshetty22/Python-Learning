'''
Loops — Question 1 (Foundation, but strict)

❓ Problem:
Take an integer n from the user and print:
👉 Sum of first n natural numbers

📌 Example:
Input: 5
Output: 15

⚠️ Rules:
Use a loop (no formula)
Use either for or while

Handle edge case:
If n <= 0 → print "Invalid input"

🧠 What I’m checking here
Loop basics
Initialization
Accumulation pattern
Edge case handling

🚫 Don’t:
Use formula
Skip edge case

'''

#Answer-

n = int(input("Enter the number: "))

if n <= 0:
    print("Invalid input")
else:
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum is:", total)






