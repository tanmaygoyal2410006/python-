"""
Given a string s, the task is to arrange the string according to the frequency of each 
character, in ascending order. If two elements have the same frequency, then they are 
sorted in lexicographical order.
Examples:
Input: s = "geeksforgeeks"
Output: forggkksseee Explanation: All the characters with minimum frequency will occur first and the one 
with same frequency will be arranged lexicographically.
Input: s = "abc"
Output: abc
Explanation: The frequency is one for all characters hence they'll be arranged 
lexicographically"
"""
from collections import Counter

def sort_by_freq(s):
    freq = Counter(s)
    
    res = sorted(s, key=lambda x: (freq[x], x))
    
    return ''.join(res)
