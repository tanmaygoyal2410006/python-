"""
Question:
Divide array into 2 subsets with equal sum and size condition.
"""

class Solution:
    def tugOfWar(self, arr):
        total = sum(arr)
        n = len(arr)
        target = total // 2
        
        from itertools import combinations
        
        for r in [n//2]:
            for comb in combinations(arr, r):
                if sum(comb) == target:
                    return [list(comb), list(set(arr)-set(comb))]
