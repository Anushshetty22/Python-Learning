"""
Question 6 — Username Generator
📌 Task:
Ask user for:
First name
Last name
Birth year
Create a username using this rule:

👉 Username format:
first 3 letters of first name + last 3 letters of last name + last 2 digits of birth year
🎯 Example:

Input:
First name: Anush
Last name: Sharma
Birth year: 2003

Output:
Username: Anrma03

⚠️ Important Points:
👉 Use:
String slicing (name[:3], etc.)
Convert birth year to string

⚠️ Edge Thinking (slight challenge)
👉 Assume:
Names are at least 3 characters long (for now)

🎯 What this tests
String slicing
Type conversion (int → str)
Combining variables
Logical thinking

💡 Hint (if needed)
👉 Think:
How to get first 3 letters?
How to get last 3 letters?
How to get last 2 digits of year?
"""
#Answer-

first_name = input("Enter the First Name: ")
last_name = input("Enter the Last Name: ")
birth_year = input("Enter the Birth Year: ")

user_name = first_name[:3] + last_name[-3:] + birth_year[-2:]

print("The Generated Username is:", user_name)