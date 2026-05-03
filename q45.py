"""
Question: Prefix Sum of Matrix (2D Array)

Given a integer matrix (or 2D array) a[][] of dimensions n * m.
Also, given another 2-D array query[][] of dimensions q * 4.

For each query, find the sum of all the elements of the rectangular 
matrix whose top left corner is (query[i][0], query[i][1]) 
and bottom right corner is (query[i][2], query[i][3]).

Example:
Input:
n = 3, m = 3, q = 2 
a[][] = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
query[][] = [
 [0, 0, 2, 2],
 [1, 0, 2, 1]
]

Output:
45
24
"""

class Solution:
    def sumQuery(self, n, m, a, q, queries):
        # Step 1: Create prefix sum matrix
        prefix = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                prefix[i][j] = a[i][j]
                
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j-1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]
        
        result = []
        
        # Step 2: Answer each query
        for query in queries:
            r1, c1, r2, c2 = query
            
            total = prefix[r2][c2]
            
            if r1 > 0:
                total -= prefix[r1-1][c2]
            if c1 > 0:
                total -= prefix[r2][c1-1]
            if r1 > 0 and c1 > 0:
                total += prefix[r1-1][c1-1]
            
            result.append(total)
        
        return result
