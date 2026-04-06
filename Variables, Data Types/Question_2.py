"""
Question 2

Ask the user for:
Their name
Their birth year
Calculate their current age using this formula:
age = current_year - birth_year

👉 Assume current year = 2026 (hardcode it)

Print output like:
Hello X, you are Y years old.
⚠️ Important Twist:
👉 input() always gives string

So you must:

Convert birth year into integer before calculation
🎯 What this tests
input()
Type conversion (str → int)
Basic calculation
Real-world thinking
💡 Small Hint (don’t skip thinking)

👉 If you try to subtract string from int → error
So think:

“What should I convert, and when?”
"""

name = input("What is your Name:")

birth_year = int(input("Enter your Birth Year:"))

current_year = 2026

age = current_year - birth_year

print(f"The age of the {name} is {age} ")