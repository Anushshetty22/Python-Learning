'''
Question 7 — Salary Bonus System

❓ Problem:

Take input:
Salary
Years of experience

📊 Rules:
👉 If experience ≥ 5 years:
If salary ≥ 50,000 → 20% bonus
Otherwise → 10% bonus
👉 If experience < 5 years:
No bonus
🧾 Output:
Print the final salary after adding bonus

⚠️ Requirements:
Use nested conditions
No hardcoding
Output should be clean (prefer formatted output)

🧠 What this tests:
Nested if
Multiple conditions
Real-world logic flow

'''

#Answer-

salary = int(input("Enter the salary: "))
years = int(input("Enter the years of experience: "))

if years >= 5:
    if salary >= 50000:
        final_salary = salary + (salary * 0.2)
    else:
        final_salary = salary + (salary * 0.1)
else:
    final_salary = salary

print("Final salary:", final_salary)




