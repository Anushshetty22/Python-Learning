'''
Question 9 — Electricity Bill (Slab Logic)

❓ Problem:
Take units consumed as input and calculate total bill:

📊 Slabs:
Units	Rate
0 – 100	₹5/unit
101 – 200	₹7/unit
201 and above	₹10/unit

⚠️ VERY IMPORTANT (Trap)
👉 This is slab-based, NOT flat rate

🧠 What that means:
If units = 250

You DON’T do:
250 × 10 ❌

You DO:
100 × 5  
+ 100 × 7  
+ 50 × 10

⚠️ Requirements:
Use if-elif-else
Correct slab calculation
Clean output
'''

#Answer-

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Total bill:", bill)

 