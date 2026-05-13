'''
Loops — Question 8 (Print All Prime Numbers)

❓ Problem:
Take an integer n and print:

👉 All prime numbers from 1 to n
📌 Example:
Input: 10
Output:
2
3
5
7

⚠️ Rules:
Use loops
No shortcuts
Don’t manually list numbers

🧠 What this tests:
Nested loops
Reusing previous logic
Loop inside loop (important skill)

💡 Think
For every number from 1 → n:
👉 Check if that number is prime
👉 If yes, print it
That’s the overall idea.
'''

#Answer-

n = int(input("Enter the number: "))

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)

        
        


    
    


