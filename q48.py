"""
Question:
arr[i] covers [i-arr[i], i+arr[i]]
Find minimum sprinklers to cover 0 to n-1.
"""

class Solution:
    def minSprinklers(self, arr, n):
        intervals = []
        
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n-1, i + arr[i])
                intervals.append((left, right))
        
        intervals.sort()
        
        count = 0
        i = 0
        curr_end = 0
        
        while curr_end < n:
            farthest = curr_end
            while i < len(intervals) and intervals[i][0] <= curr_end:
                farthest = max(farthest, intervals[i][1] + 1)
                i += 1
            
            if farthest == curr_end:
                return -1
            
            count += 1
            curr_end = farthest
        
        return count
