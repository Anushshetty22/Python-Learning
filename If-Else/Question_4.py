'''
If-Else — Question 4 (Real Logic)

❓ Problem:
Take three numbers as input from the user and print:
👉 The largest number

⚠️ Rules:
Use only if-elif-else (no max() allowed)
Handle all cases correctly
Inputs should be taken separately

⚠️ This is NOT trivial

Edge cases to think about:
What if two numbers are equal?
What if all three are equal?
What if largest appears in different positions?

🚫 Avoid weak logic like:
Only comparing two numbers
Missing equality cases

'''

#Answer-

num_1 = int(input("Enter the number 1: "))
num_2 = int(input("Enter the number 2: "))
num_3 = int(input("Enter the number 3: "))

if num_1 == num_2 == num_3:
    print("All are equal")
elif num_1 >= num_2 and num_1 >= num_3:
    print("Number 1 is greatest")
elif num_2 >= num_1 and num_2 >= num_3:
    print("Number 2 is greatest")
else:
    print("Number 3 is greatest")