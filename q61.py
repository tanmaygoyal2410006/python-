"""
Given a string s consisting of balanced parentheses, calculate the score of the string 
based on the following rules:"()" has a score of 1.
• "AB" has a score of A + B, where A and B are balanced parentheses strings.
• "(A)" has a score of 2 × score(A), where A is a balanced parentheses string.
Note: Test cases are generated such that the score will fit within a 32-bit integer.
Examples:
Input: s = "()()"
Output: 2
Explanation: The string str is of the form "ab", that makes the total score = (score of a) 
+ (score of b) = 1 + 1 = 2.
Input: s = "(()(()))"
Output: 6
Explanation: The string str is of the form "(a(b))" which makes the total score = 2 × 
((score of a) + 2 × (score of b)) = 2 × (1 + 2 × (1)) = 6.
Input: s = "((()))"Output: 4
Explanation: The string str is of the form "((a))" which makes the total score = 2 × (2 
× (score of a)) = 2 × (2 × (1)) = 4.
"""

def score_parentheses(s):
    stack = [0]
    
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            val = stack.pop()
            score = max(2 * val, 1)
            stack[-1] += score
    
    return stack[0]
