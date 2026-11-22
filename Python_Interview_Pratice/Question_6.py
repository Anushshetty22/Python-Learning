# Set 2 | Question 6/40: Two Sum
# Difficulty: Easy-Medium
# Category: Core Python
#
# Given a list of integers and a target, find two numbers
# whose sum equals the target.
#
# Print their indices as a list, with the smaller index first.
# If no matching pair exists, print None.
#
# Example input:
# numbers = [2, 7, 11, 15]
# target = 9
#
# Expected output:
# [0, 1]
#
# Additional test cases:
# numbers = [3, 2, 4], target = 6
# Expected output: [1, 2]
#
# numbers = [3, 3], target = 6
# Expected output: [0, 1]
#
# numbers = [-4, 1, 6, 8], target = 2
# Expected output: [0, 2]
#
# numbers = [1, 2, 3], target = 10
# Expected output: None
#
# numbers = [], target = 5
# Expected output: None
#
# numbers = [5], target = 10
# Expected output: None
#
# Constraints:
# 1. Indices start at 0.
# 2. You cannot use the same list element twice.
# 3. Duplicate values and negative numbers are allowed.
# 4. There is at most one valid pair of indices.
# 5. Do not modify the original list.
# 6. Use the supplied values directly; input() is not required.
# 7. A function is optional.
# 8. Do not use external libraries or classes.

numbers = [2, 7, 11, 15]
target = 9


result = None

for i in range(0,len(numbers)-1) :
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j]== target:
            result = [i, j]
            

print(result)