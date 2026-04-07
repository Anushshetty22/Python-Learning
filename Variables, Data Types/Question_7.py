"""
Question 7 — Temperature Converter

📌 Task:
Ask user for temperature in Celsius

Convert it into Fahrenheit using formula:
F = (C * 9/5) + 32

Print output:
Temperature in Fahrenheit is: X

⚠️ Challenge Twist
👉 Also print:
Data type of input value
Data type after conversion

🎯 Example
Enter temperature in Celsius: 25
Temperature in Fahrenheit is: 77.0
Type of Celsius: <class 'float'>
Type of Fahrenheit: <class 'float'>

🎯 What this tests
Type conversion (input → float)
Arithmetic formula
type() usage
Clean output

💡 Hint (if needed)
👉 Remember:
input() → string
You must convert before calculation """

#Answer-

c = float(input("Enter temperature in Celsius:"))

f = (c * 9/5) + 32

print("Temperature in Fahrenheit is:", f)

print("Type of Celsius:", type(c))

print("Type of Fahrenheit:", type(f))



