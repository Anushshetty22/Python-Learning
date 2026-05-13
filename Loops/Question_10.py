'''
Loops — Question 10 (Pattern Printing)

❓ Problem:
Take an integer n and print this pattern:

For n = 4:
*
**
***
****

⚠️ Rules:
Use nested loops
Don’t hardcode stars
Each row should be on a new line

🧠 What this tests:
Outer loop → controls rows
Inner loop → controls how many * per row

'''

#Answer-

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()