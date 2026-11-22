# Set 2 | Question 10/40: Clean and Summarize Transactions
# Difficulty: Easy-Medium
# Category: Mixed Data Engineering Scenario
#
# Given a list of transactions, calculate the total valid
# transaction amount for each city.
#
# A transaction is valid only when:
# 1. Its status is "completed".
# 2. Its amount exists and is not None.
# 3. Its amount is greater than or equal to 0.
#
# Skip invalid transactions.
# Print a dictionary mapping each city to its valid total.
# Include a city only if it has at least one valid transaction.
#
# Example input:
# transactions = [
#     {"city": "Mumbai", "amount": 1200, "status": "completed"},
#     {"city": "Delhi", "amount": 800, "status": "completed"},
#     {"city": "Mumbai", "amount": 500, "status": "completed"},
#     {"city": "Pune", "amount": None, "status": "completed"},
#     {"city": "Delhi", "amount": -100, "status": "completed"},
#     {"city": "Pune", "status": "completed"},
#     {"city": "Mumbai", "amount": 900, "status": "pending"}
# ]
#
# Expected output:
# {"Mumbai": 1700, "Delhi": 800}
#
# Additional test cases:
# Input: []
# Expected output: {}
#
# Input: [
#     {"city": "Pune", "amount": None, "status": "completed"},
#     {"city": "Delhi", "amount": 500, "status": "pending"}
# ]
# Expected output: {}
#
# Input: [
#     {"city": "Pune", "amount": 0, "status": "completed"}
# ]
# Expected output: {"Pune": 0}
#
# Input: [
#     {"city": "Delhi", "amount": 100, "status": "completed"},
#     {"city": "Delhi", "amount": 200, "status": "completed"}
# ]
# Expected output: {"Delhi": 300}
#
# Constraints:
# 1. Every record has a non-empty "city" and a "status" string.
# 2. "amount" may be missing, None, or an integer.
# 3. City and status matching are case-sensitive.
# 4. Do not modify the original list or its dictionaries.
# 5. Use the supplied values directly; input() is not required.
# 6. A function is optional.
# 7. Do not use external libraries or classes.



def correct_values(transactions):
    final_value = {}

    for i in transactions:
        city = i.get("city")
        amount = i.get("amount")
        status = i.get("status")

        # Check for None before comparing the amount with 0.
        if status == "completed" and amount is not None and amount >= 0:
            if city in final_value:
                final_value[city] = final_value[city] + amount
            else:
                final_value[city] = amount

    return final_value


transactions = [
    {"city": "Mumbai", "amount": 1200, "status": "completed"},
    {"city": "Delhi", "amount": 800, "status": "completed"},
    {"city": "Mumbai", "amount": 500, "status": "completed"},
    {"city": "Pune", "amount": None, "status": "completed"},
    {"city": "Delhi", "amount": -100, "status": "completed"},
    {"city": "Pune", "status": "completed"},
    {"city": "Mumbai", "amount": 900, "status": "pending"}
]

result = correct_values(transactions)
print(result)
