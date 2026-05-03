"""
You are given an array arr[] of strings. Your have to sort the array in ascending order 
based on the lengths of the strings. If two strings have the same length, maintain their 
original relative order.
Examples:
Input: arr[] = ["GeeksforGeeeks", "I", "from", "am"]
Output: ["I", "am", "from", "GeeksforGeeks"]
Explanation: The strings are sorted in increasing order of their lengths, starting from 
the shortest string "I" to the longest one "GeeksforGeeeks".
Input: arr[] = ["You", "are", "beautiful", "looking"]
Output: ["You", "are", "looking", "beautiful"]
Explanation: The strings are sorted by length: "You", "are", "looking", and then 
"beautiful", with the shortest words appearing first and the longest last."
"""
def sort_by_length(arr):
    return sorted(arr, key=len)
