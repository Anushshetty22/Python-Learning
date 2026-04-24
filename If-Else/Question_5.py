'''
If-Else — Question 5 (Upgraded)

❓ Problem:
Take an integer input (year) from the user and check:
👉 If the year is a leap year, print:
Leap year
👉 Otherwise, print:
Not a leap year

⚠️ Real Logic (this is where it gets interesting)
A year is a leap year if:
It is divisible by 4
BUT if it is divisible by 100 → it is NOT a leap year
EXCEPT if it is divisible by 400 → it IS a leap year

🧠 Example:
2000 → Leap year ✅
1900 → Not leap ❌
2024 → Leap year ✅
2023 → Not leap ❌

⚠️ Rules:
Use if-elif-else
No shortcuts
Handle logic properly (this is NOT a simple condition)

'''

# Answer-

year = int(input("Enter the year :"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("Its a Leap Year")
else:
    print("Its not a Leap year")