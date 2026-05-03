"""
Question:
Given array arr[], in one operation you can replace any element with half of its value.
Return minimum operations to make sum <= half of original sum.
"""

import heapq

class Solution:
    def minSteps(self, arr):
        total = sum(arr)
        target = total / 2
        
        heap = [-x for x in arr]
        heapq.heapify(heap)
        
        operations = 0
        current = total
        
        while current > target:
            largest = -heapq.heappop(heap)
            half = largest / 2
            current -= half
            heapq.heappush(heap, -half)
            operations += 1
        
        return operations
