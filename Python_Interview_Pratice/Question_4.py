# Set 1 | Question 4/40: Calculate Total Sales by Product
# Difficulty: Easy–Medium
# Category: Python Data Processing
#
# Given a list of sales records, calculate the total amount
# sold for each product.
#
# Each record contains a product name and an amount.
# If a product appears multiple times, add its amounts together.
# Store the results in a dictionary and print it.
#
# Example input:
# sales = [
#     {"product": "Laptop", "amount": 50000},
#     {"product": "Mouse", "amount": 500},
#     {"product": "Laptop", "amount": 60000},
#     {"product": "Keyboard", "amount": 1500},
#     {"product": "Mouse", "amount": 700}
# ]
#
# Expected output:
# {"Laptop": 110000, "Mouse": 1200, "Keyboard": 1500}
#
# Additional test cases:
# Input: []
# Expected output: {}
#
# Input: [{"product": "Mouse", "amount": 500}]
# Expected output: {"Mouse": 500}
#
# Input: [
#     {"product": "Mouse", "amount": 0},
#     {"product": "Mouse", "amount": 700}
# ]
# Expected output: {"Mouse": 700}
#
# Constraints:
# 1. Every record contains "product" and "amount".
# 2. Product names are case-sensitive strings.
# 3. Amounts are non-negative integers.
# 4. Do not modify the original sales records.
# 5. Use the supplied data directly; input() is not required.
# 6. A function is optional.
# 7. Do not use external libraries or classes.



sales = [
     {"product": "Laptop", "amount": 50000},
     {"product": "Mouse", "amount": 500},
     {"product": "Laptop", "amount": 60000},
     {"product": "Keyboard", "amount": 1500},
     {"product": "Mouse", "amount": 700}
 ]

sales_result= {}


for i in sales :
    product = i.get("product")
    amount = i.get("amount")

    if product in sales_result :
        sales_result[product] = sales_result[product]+ amount
    else:
        sales_result[product] = amount
    


print(sales_result)