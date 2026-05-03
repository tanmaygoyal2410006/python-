"""
Question:
Count elements <= x in sorted rotated array.
"""

class Solution:
    def count(self, arr, x):
        return sum(1 for num in arr if num <= x)
