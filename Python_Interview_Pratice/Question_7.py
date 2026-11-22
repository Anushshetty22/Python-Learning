# Set 2 | Question 7/40: Remove Duplicate Customer Records
# Difficulty: Easy-Medium
# Category: Python Data Processing
#
# Given a list of customer records, remove duplicate customers
# based on their "id".
#
# If an id appears more than once, keep only the FIRST record
# with that id, even if later records have different names.
#
# Print the resulting list of complete customer dictionaries.
# Preserve the order in which the customers first appeared.
#
# Example input:
# customers = [
#     {"id": 1, "name": "Anush"},
#     {"id": 2, "name": "Rahul"},
#     {"id": 1, "name": "Anush Shetty"},
#     {"id": 3, "name": "Priya"},
#     {"id": 2, "name": "Rahul Kumar"}
# ]
#
# Expected output:
# [
#     {"id": 1, "name": "Anush"},
#     {"id": 2, "name": "Rahul"},
#     {"id": 3, "name": "Priya"}
# ]
#
# Additional test cases:
# Input: []
# Expected output: []
#
# Input: [
#     {"id": 1, "name": "A"},
#     {"id": 2, "name": "A"}
# ]
# Expected output:
# [{"id": 1, "name": "A"}, {"id": 2, "name": "A"}]
#
# Input: [
#     {"id": 5, "name": "First"},
#     {"id": 5, "name": "Second"},
#     {"id": 5, "name": "Third"}
# ]
# Expected output:
# [{"id": 5, "name": "First"}]
#
# Constraints:
# 1. Every record contains an integer "id" and a string "name".
# 2. Only the id determines whether a customer is a duplicate.
# 3. Do not modify the original list or its dictionaries.
# 4. Use the supplied values directly; input() is not required.
# 5. A function is optional.
# 6. Do not use external libraries or classes.





def find_duplicate(customers):

    result= []
    seen_ids = []

    for i in customers:
        if i.get("id") not in seen_ids:
            seen_ids.append(i.get("id")) 
            result.append(i)


    return result


customers = [
    {"id": 1, "name": "Anush"},
    {"id": 2, "name": "Rahul"},
    {"id": 1, "name": "Anush Shetty"},
    {"id": 3, "name": "Priya"},
    {"id": 2, "name": "Rahul Kumar"}
         ]

final_result = find_duplicate(customers)
print(final_result)