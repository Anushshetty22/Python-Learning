"""Question 1

Create 4 variables:
name → your name (string)
age → your age (integer)
height → your height in meters (float)
is_student → whether you are a student (boolean)

Print all values in one sentence like:
My name is X, I am Y years old, my height is Z meters, and student status is W
Print the data type of each variable using type()

⚠️ Slight Challenge Twist:

👉 Convert:

age into a string
height into an integer

And print them again.

🎯 What this question tests
Variable creation
Data types (int, float, str, bool)
Type checking (type())
Type conversion

👉 These are core fundamentals in Python"""

#Answer-

name = "Anush"
age = 22
height = 1.64592 
is_student = False

# Original print
print(f"My name is {name}, I am {age} years old, my height is {height} meters, and student status is {is_student}.")

# Print data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# Type conversion
age = str(age)
height = int(height)

# Print after conversion
print(f"My name is {name}, I am {age} years old, my height is {height} meters, and student status is {is_student}.")

# Print data types after conversion
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))