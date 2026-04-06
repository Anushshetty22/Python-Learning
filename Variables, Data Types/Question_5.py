"""
Question 5 — Simple Interest Calculator

📌 Task:

Ask user for:
Principal amount
Rate of interest (in %)
Time (in years)

Calculate Simple Interest using formula:
SI = (P * R * T) / 100

Calculate total amount:
total_amount = P + SI

🎯 Output Example:
Simple Interest is: X
Total Amount is: Y

⚠️ Important Points:
👉 Convert:
Principal → float
Rate → float
Time → float or int (your choice)

💡 Slight Challenge
👉 Format output to 2 decimal places (like money)

🎯 What this tests
Multiple inputs
Type conversion
Formula implementation
Clean output
"""

P = float(input("Enter the Principal amount:"))

R = float(input("Enter the Rate of Interest:"))

T = float(input("Enter the time in years:"))

SI = (P * R * T) / 100

total_amount = P + SI

print(f"Simple Interest is:{SI:.2f}")

print(f"Total Amount is:{total_amount:.2f}")