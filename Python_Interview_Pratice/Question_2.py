# Set 1 | Question 2/40: Filter Transaction Records
# Difficulty: Easy
# Category: Python Data Processing
#
# Write a function filter_transactions(transactions) that returns
# a list containing only transactions that meet BOTH conditions:
# 1. The status is "completed".
# 2. The amount is greater than or equal to 1000.
#
# Preserve the original order and include the entire dictionary
# for each matching transaction.
#
# Example input:
# transactions = [
#     {"id": 1, "amount": 1500, "status": "completed"},
#     {"id": 2, "amount": 2000, "status": "pending"},
#     {"id": 3, "amount": 500, "status": "completed"},
#     {"id": 4, "amount": 1000, "status": "completed"}
# ]
#
# Expected output:
# [
#     {"id": 1, "amount": 1500, "status": "completed"},
#     {"id": 4, "amount": 1000, "status": "completed"}
# ]
#
# Additional test cases:
# Input: []
# Expected output: []
#
# Input: [{"id": 5, "amount": 999, "status": "completed"}]
# Expected output: []
#
# Input: [{"id": 6, "amount": 1000, "status": "completed"}]
# Expected output:
# [{"id": 6, "amount": 1000, "status": "completed"}]
#
# Constraints:
# 1. Every transaction contains "id", "amount", and "status".
# 2. Amounts are non-negative numbers.
# 3. Status matching is case-sensitive.
# 4. Do not modify the original list or its dictionaries.
# 5. Do not use external libraries or classes.

transactions = [
     {"id": 1, "amount": 1500, "status": "completed"},
     {"id": 2, "amount": 2000, "status": "pending"},
     {"id": 3, "amount": 500, "status": "completed"},
     {"id": 4, "amount": 1000, "status": "completed"}
 ]


def filter_transactions(transactions):
    transactions_result = []

    for i in transactions:
        if i.get("status") == "completed" and i.get("amount") >= 1000:
            transactions_result.append(i) 
            
    return transactions_result


result = filter_transactions(transactions)

print(result)