'''
Question 8 — Login System (Nested Logic)
❓ Problem:

Take input:
Username
Password
🔐 Correct credentials:
username: admin
password: 1234

📊 Logic:

👉 If username is incorrect:
Invalid username

👉 If username is correct BUT password is wrong:
Invalid password

👉 If both are correct:
Login successful

⚠️ Requirements:
Use nested if
Don’t check password first (important)
Follow proper flow

🧠 What this tests:
Decision hierarchy
Nested conditions
Real-world logic (very common in interviews)
'''

#Answer-

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")

