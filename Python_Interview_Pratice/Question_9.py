# Set 2 | Question 9/40: Group Employees by Department
# Difficulty: Easy-Medium
# Category: Python Data Processing
#
# Given a list of employee records, group employee names
# by their department.
#
# Print a dictionary where:
# - Each key is a department name.
# - Each value is a list of employee names in that department.
#
# Preserve the original order of names within each department.
#
# Example input:
# employees = [
#     {"name": "Anush", "department": "Engineering"},
#     {"name": "Priya", "department": "Sales"},
#     {"name": "Rahul", "department": "Engineering"},
#     {"name": "Neha", "department": "HR"},
#     {"name": "Amit", "department": "Sales"}
# ]
#
# Expected output:
# {
#     "Engineering": ["Anush", "Rahul"],
#     "Sales": ["Priya", "Amit"],
#     "HR": ["Neha"]
# }
#
# Additional test cases:
# Input: []
# Expected output: {}
#
# Input: [{"name": "A", "department": "HR"}]
# Expected output: {"HR": ["A"]}
#
# Input: [
#     {"name": "A", "department": "Sales"},
#     {"name": "B", "department": "Sales"}
# ]
# Expected output: {"Sales": ["A", "B"]}
#
# Input: [
#     {"name": "A", "department": "HR"},
#     {"name": "A", "department": "HR"}
# ]
# Expected output: {"HR": ["A", "A"]}
#
# Constraints:
# 1. Every record contains "name" and "department" as strings.
# 2. Department names are case-sensitive.
# 3. Keep every employee entry, including repeated names.
# 4. Do not modify the original list or its dictionaries.
# 5. Use the supplied values directly; input() is not required.
# 6. A function is optional.
# 7. Do not use external libraries or classes.


def name_by_department(employees):

    final_list = {}
    name_list = []

    for i in employees :
        department = i.get("department")
        name = i.get("name")
        if department not in final_list:
            final_list[department] = [name]
        else:
            final_list[department].append(name)

            

    return final_list



employees = [
    {"name": "Anush", "department": "Engineering"},
    {"name": "Priya", "department": "Sales"},
    {"name": "Rahul", "department": "Engineering"},
    {"name": "Neha", "department": "HR"},
    {"name": "Amit", "department": "Sales"}
     ]

result = name_by_department(employees)
print(result)