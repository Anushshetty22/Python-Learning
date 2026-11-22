# Set 2 | Question 8/40: Find Common Elements in Two Lists
# Difficulty: Easy-Medium
# Category: Core Python
#
# Given two lists of integers, find the values present in BOTH.
# Print each common value only once, even if it appears multiple
# times in either list.
#
# Preserve the order in which the values first appear in list1.
#
# Example input:
# list1 = [4, 2, 7, 2, 9, 4]
# list2 = [2, 4, 4, 8]
#
# Expected output:
# [4, 2]
#
# Additional test cases:
# list1 = [1, 2, 3], list2 = [4, 5, 6]
# Expected output: []
#
# list1 = [3, 3, 3], list2 = [3, 3]
# Expected output: [3]
#
# list1 = [], list2 = [1, 2]
# Expected output: []
#
# list1 = [1, 2], list2 = []
# Expected output: []
#
# list1 = [-2, 0, 5], list2 = [5, -2]
# Expected output: [-2, 5]
#
# Constraints:
# 1. Both lists contain only integers and may be empty.
# 2. Duplicate values and negative numbers are allowed.
# 3. Do not modify or sort the original lists.
# 4. Use the supplied values directly; input() is not required.
# 5. A function is optional.
# 6. Do not use external libraries or classes.


def find_unique(list1,list2):

    result = []

    for i in list1:
        if i not in result and i in list2:
            result.append(i)
       
    return result



list1 = [4, 2, 7, 2, 9, 4]
list2 = [2, 4, 4, 8]

result = find_unique(list1,list2)
print(result)
