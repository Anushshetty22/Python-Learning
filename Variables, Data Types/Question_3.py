"""
Create two variables:
a = 10
b = 20
Swap their values
👉 After swapping:
a = 20
b = 10
⚠️ Rules:

❌ Do NOT use a third variable (no temp)
❌ Do NOT hardcode new values

✅ You must swap using Python logic

🎯 What this tests
Understanding of variables
Assignment behavior
Logical thinking
💡 Hint (if needed)

👉 Think:

“Can Python assign multiple values in one line?”
"""

a, b = 10, 20

print("Before swap-")
print("a=", a)
print("b=", b)

a, b = b, a   

print("After swap-")
print("a=", a)
print("b=", b)
