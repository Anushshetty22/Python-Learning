# Set 1 | Question 5/40: Find the Missing Number
# Difficulty: Easy
# Category: Core Python
#
# Given an integer n and a list of numbers, find and print
# the single missing number from the range 1 through n.
#
# The list contains every number in that range except one.
# The numbers may appear in any order.
#
# Example input:
# n = 5
# numbers = [3, 1, 5, 2]
#
# Expected output:
# 4
#
# Additional test cases:
# n = 5, numbers = [2, 3, 4, 5]
# Expected output: 1
#
# n = 5, numbers = [1, 2, 3, 4]
# Expected output: 5
#
# n = 3, numbers = [3, 1]
# Expected output: 2
#
# n = 1, numbers = []
# Expected output: 1
#
# Constraints:
# 1. n is an integer greater than or equal to 1.
# 2. The list contains exactly n - 1 distinct integers.
# 3. Every number in the list is between 1 and n, inclusive.
# 4. Exactly one number is missing.
# 5. Do not modify the original list.
# 6. Use the supplied values directly; input() is not required.
# 7. A function is optional.
# 8. Do not use external libraries or classes.


n = 5
numbers = [3, 1, 5, 2]


for j in range(1, n + 1):
    if j not in numbers:
        print(f"Expected output:{j}")