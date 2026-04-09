"""
Question 15 — Password Strength Checker

📌 Task:
Ask user to enter a password
Check password strength based on rules:

👉 Conditions:
Length ≥ 8
Contains at least:
1 digit
1 uppercase letter
1 lowercase letter

🎯 Output:
If all conditions satisfied →
Strong Password
Else →
Weak Password

💡 Hint (important)
👉 You can use:
len(password)
Loop through characters OR use:
.isdigit()
.isupper()
.islower()

🎯 Example
Enter password: Abc12345
Strong Password
Enter password: abc
Weak Password

🎯 What this tests
Strings
Conditions
Logic building
Real-world validation
"""
#Answer-

password = input("Enter the password: ")

length_condition = len(password) >= 8

has_digit = False
has_upper = False
has_lower = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True

if length_condition and has_digit and has_upper and has_lower:
    print("Strong Password")
else:
    print("Weak Password")