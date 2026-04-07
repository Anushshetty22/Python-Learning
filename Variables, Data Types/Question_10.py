"""
Question 10 — Email Masking

📌 Task:
Ask user for their email address
Mask the email like this:

👉 Rule:
Show first 2 characters of username
Replace remaining username characters with *
Keep domain unchanged

🎯 Example:
Input: anush123@gmail.com
Output: an*****@gmail.com

🧠 Breakdown
Email has 2 parts:
username@domain
So:
Extract username
Extract domain
Mask username

⚠️ Important Points
👉 Use:
String slicing
split('@')

💡 Hint (if needed)
👉 Steps:
Split email → username, domain
Keep first 2 letters → username[:2]
Remaining length → replace with *

🎯 What this tests
String splitting
Slicing
String manipulation
Logic building
"""

#Answer-

email = input("Enter your email: ")

username, domain = email.split('@')

visible = username[:2]

stars = "*" * (len(username)-2)

masked_email = visible + stars + "@" + domain

print("Masked Email: ",masked_email)