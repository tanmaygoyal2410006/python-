"""
You are given two strings, s1 and s2, where s1 contains distinct lowercase vowels (a, 
e, i, o, u), and s2 contains lowercase English letters. Your task is to find the length of 
the shortest contiguous substring within s2 that contains all the vowels present in s1 at 
least once, in any order.
Note: If there is no such substring in s2, return -1.
Examples:
Input: s1 = "ae", s2 = "acbaudeq"
Output: 4
Explanation: The shortest substring of "acbaudeq" that contains both vowels 'a' and 'e' 
from s1 = "ae" is "aude", which has length 4.
Input: s1 = "iou", s2 = "iuixoiu"
Output: 3
Explanation: The shortest substring of "iuixoiu" that contains all vowels 'i', 'o', and 'u' 
from s1 = "iou" is "oiu", which has length 3.
Input: s1 = "aeiou", s2 = "uoiee Output: -1
Explanation: The string s2 = "uoiee" is missing the vowel 'a' from s1 = "aeiou", so no 
substring can contain all required vowels, and the answer is -1."
"""
def shortest_substring(s1, s2):
    need = set(s1)
    left = 0
    count = {}
    formed = 0
    
    ans = float('inf')
    
    for right in range(len(s2)):
        ch = s2[right]
        
        if ch in need:
            count[ch] = count.get(ch, 0) + 1
            if count[ch] == 1:
                formed += 1
        
        while formed == len(need):
            ans = min(ans, right - left + 1)
            
            if s2[left] in count:
                count[s2[left]] -= 1
                if count[s2[left]] == 0:
                    formed -= 1
            
            left += 1
    
    return ans if ans != float('inf') else -1
