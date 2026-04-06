"""
Question 4 — Type Conversion + Calculation

📌 Task:
Ask user for:
Price of 1 item
Quantity of items

Calculate:
total_cost = price * quantity

Print:
Total cost is: X

⚠️ Important Twist
👉 User may enter:
price as decimal (e.g., 99.99)
quantity as whole number

So:
Convert price → float
Convert quantity → int

⚠️ Challenge Twist (Important)
👉 Add 10% tax to total cost

Formula:
tax = total_cost * 0.10
final_amount = total_cost + tax

🎯 Final Output Example
Total cost is: 200
Tax is: 20
Final amount to pay: 220

🎯 What this tests
input() handling
Type conversion (float, int)
Arithmetic operations
Real-world calculation
"""


price_of_item = float(input("Please enter the price of the item:"))

quantity_of_item = int(input("Enter the quantity of the item:"))

total_cost = price_of_item * quantity_of_item

print("Total Cost is:", total_cost)

tax = total_cost * 0.10

final_amount = total_cost + tax

print("Tax is :",tax)

print(f"Final amount to pay: {final_amount:.2f}")
