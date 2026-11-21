# Set 1 | Question 3/40: Check Whether Two Strings Are Anagrams
# Difficulty: Easy–Medium
# Category: Core Python
#
# Write a function are_anagrams(word1, word2) that returns True
# if the two strings are anagrams. Otherwise, return False.
#
# Two strings are anagrams if they contain the same characters
# with the same number of occurrences, possibly in a different order.
#
# Example input:
# word1 = "listen"
# word2 = "silent"
#
# Expected output:
# True
#
# Additional test cases:
# word1 = "hello", word2 = "world" -> False
# word1 = "aabb",  word2 = "baba"  -> True
# word1 = "aab",   word2 = "abb"   -> False
# word1 = "abc",   word2 = "ab"    -> False
# word1 = "",      word2 = ""      -> True
# word1 = "a",     word2 = ""      -> False
#
# Constraints:
# 1. Both strings contain only lowercase English letters.
# 2. Either string may be empty.
# 3. Repeated characters must appear the same number of times
#    in both strings.
# 4. Return a Boolean value, rather than only printing it.
# 5. Use the supplied values directly; input() is not required.
# 6. Do not use external libraries or classes.



word1 = "listen"
word2 = "silent"


def are_anagrams(word1, word2):

    count_word1 = {}
    count_word2 = {}

    for i in word1:
        if i in count_word1:
            count_word1[i] = count_word1[i] + 1
        else:
            count_word1[i] = 1

    for i in word2:
        if i in count_word2:
            count_word2[i] = count_word2[i] + 1
        else:
            count_word2[i] = 1

    if count_word1 == count_word2 :
        return True
    else:
        return False


result = are_anagrams(word1, word2)

print(result)