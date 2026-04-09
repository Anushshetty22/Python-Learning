"""
Question 13 — Discount Calculator

📌 Task:
Ask user for:
Total purchase amount
Apply discount based on amount:
Amount	Discount
≥ 1000	20%
≥ 500	10%
< 500	No discount
Calculate:
Discount amount
Final amount after discount

🎯 Output Example
Enter total amount: 1200
Discount applied: 240.00
Final amount: 960.00
⚠️ Important Points

👉 Use:
if / elif / else
Convert input to float
Format output to 2 decimal places

💡 Hint (if needed)
👉 Think:
Check highest condition first (>= 1000)
Then next (>= 500)

🎯 What this tests
Conditions (priority order)
Arithmetic logic
Real-world scenario
"""

amount = float(input("Enter total amount: "))

if amount >= 1000:
    discount = amount * 0.20
elif amount >= 500:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print(f"Discount applied: {discount:.2f}")
print(f"Final amount: {final_amount:.2f}")