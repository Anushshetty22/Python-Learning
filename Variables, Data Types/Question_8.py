"""
Question 8 — Split Bill Calculator
📌 Task:

Ask user for:
Total bill amount
Number of people
Calculate:
amount_per_person = total_bill / number_of_people

⚠️ Challenge Twist
👉 Add tip percentage:
Ask:

“Enter tip percentage (e.g., 10, 15, 20):”

Then:
tip = total_bill * (tip_percent / 100)
final_bill = total_bill + tip
amount_per_person = final_bill / number_of_people

🎯 Output Example
Each person should pay: 220.50

⚠️ Important Points
👉 Convert:
total_bill → float
number_of_people → int
tip_percent → float

💡 Slight Challenge
👉 Format output to 2 decimal places  

🎯 What this tests
Multiple inputs
Type conversions
Real-world calculation
Clean output formatting

💡 Hint (if needed)
👉 Think step-by-step:
Calculate tip
Add to bill
Divide
"""
#Answer-

total_bill = float(input("Enter the Total Bill amount: "))
number_of_people = int(input("Enter the Number of People: "))
tip_percent = float(input("Enter tip percentage (e.g., 10, 15, 20): "))

tip = total_bill * (tip_percent / 100)
final_bill = total_bill + tip

amount_per_person = final_bill / number_of_people

print(f"Each person should pay: {amount_per_person:.2f}")  