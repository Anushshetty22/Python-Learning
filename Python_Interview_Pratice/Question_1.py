# Set 1 | Question 1/40: First Non-Repeating Character
# Difficulty: Easy–Medium
# Category: Core Python
#
# Write a function first_unique_char(text) that returns the first
# character that appears exactly once in the given string.
# If no such character exists, return None.
#
# Example:
# Input: text = "swiss"
# Expected output: "w"
#
# Additional test cases:
# Input: "aabbcde"  -> Expected output: "c"
# Input: "aabb"     -> Expected output: None
# Input: ""         -> Expected output: None
# Input: "z"        -> Expected output: "z"
# Input: "AaBbA"    -> Expected output: "a"
#
# Constraints:
# 1. Matching is case-sensitive: "A" and "a" are different.
# 2. Return the first unique character in the original string order.
# 3. The input contains only English letters and may be empty.
# 4. Do not use external libraries or classes.

def first_unique_char(text):
    counts = {}

    # Count how many times each character appears.
    for char in text:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1

    # Find the first character that appears only once.
    for char in text:
        if counts[char] == 1:
            return char

    return None


text = input("Enter a string: ")
result = first_unique_char(text)
print("First non-repeating character:", result)