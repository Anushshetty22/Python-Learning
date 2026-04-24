'''
Question 6 — Triangle Validity + Type

❓ Problem:
Take 3 sides as input.

👉 First check:
If triangle is valid
(sum of any two sides > third side)

👉 If valid, print:
"Equilateral" (all equal)
"Isosceles" (any two equal)
"Scalene" (all different)

👉 If not valid:
Invalid triangle

'''

#Answer-

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")




       