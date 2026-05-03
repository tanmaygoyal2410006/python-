"""
Given a string s consisting of lowercase English letters and an integer k, your task is to 
remove exactly k characters from the string. The resulting string must be the largest 
possible in lexicographical order, while maintain the relative order of the remaining 
characters.
Examples:
Input: s = "ritz", k = 2
Output: tz 
Explaination: By removing two characters in all possible ways, we get: "ri", "rt", "rz", 
"it", "iz", and "tz". Among these, "tz" is lexicographically largest string.
Input: s = "zebra", k = 3
Output: zr 
Explaination: Removing "e", "b", and "a" results in "zr", which is lexicographically 
largest string."
"""
from def largest_after_k(s, k):
    stack = []
    
    for ch in s:
        while k > 0 and stack and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    
    return ''.join(stack[:-k] if k else stack)
