"""
Given an array arr[] of strings of equal length, where each string consists of lowercase 
English letters, find the total number of pairs of strings that differ in exactly one 
character position.
Note: Two strings differ in exactly one position if they have the same length and differ 
in exactly one index that is, all characters except one are the same.
Examples :
Input: arr[] = ["abc", "abd", "bbd"]
Output: 2
Explanation: The valid pairs are:
1. ("abc", "abd") → differ at index 2
2. ("abd", "bbd") → differ at index 0
Input: arr[] = ["def", "deg", "dmf", "xef", "dxg"]
Output: 4
Explanation: The valid pairs are:
1. ("def", "deg") → differ at index 2
2. ("def", "dmf") → differ at index 1
3. ("def", "xef") → differ at index 0
4. ("deg", "dxg") → differ at index 1 Input: arr[] = ["bcde", "bced", "bdce"]
Output: 0
Explanation: No pair differs at exactly one position."
"""
def count_pairs(arr):
    n = len(arr)
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            diff = 0
            for k in range(len(arr[i])):
                if arr[i][k] != arr[j][k]:
                    diff += 1
            if diff == 1:
                count += 1
    
    return count
