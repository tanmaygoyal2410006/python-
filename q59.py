"""
You are given two binary strings s1 and s2 of equal length, and the task is to find 
the minimum number of swaps required to make them identical. The only allowed 
operation is swapping characters between the two strings (i.e., you can 
swap s1[i] with s2[j], but not within the same string). If it is impossible to make the two 
strings equal through such swaps, return -1.
Examples:
Input: s1 = "1100", s2 = "1111"
Output: 1
Explanation: Swap the character at index 2 of s1 with the character at index 3 of s2. 
After this swap both strings become "1110", so only 1 swap is needed.
Input: s1 = "00011" , s2 = "11001"
Output: -1
Explanation: It is impossible to make both strings equal, so the answer is -1.
"""

def min_swaps(s1, s2):
    mismatches = 0
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatches += 1
    
    if mismatches % 2 != 0:
        return -1
    
    return mismatches // 2
