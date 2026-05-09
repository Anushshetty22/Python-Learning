'''
Loops — Question 2 (Digit Extraction)

❓ Problem:
Take an integer input and print:
👉 Sum of its digits

📌 Example:
Input: 1234  
Output: 10   (1 + 2 + 3 + 4)
Input: 507  
Output: 12   (5 + 0 + 7)

⚠️ Rules:
Use a loop
Don’t convert number to string
Use math logic (important)

🧠 What this tests:
Loop control
Digit extraction
Mathematical thinking

'''

#Answer-

num = int(input("Enter the Numbers: "))

total = 0

while num > 0:
    total += num % 10
    num =  num // 10
    
print("The total sum of the given digits are: ",total)



