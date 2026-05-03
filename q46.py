"""
Question:
Given matrix a[n][m] and queries with (R, C) 1-based indexing.
Construct footpath on Rth row and Cth column.
Return sum of minimum value of all sections formed.
"""

class Solution:
    def footpath(self, n, m, a, q, queries):
        ans = []
        
        for R, C in queries:
            R -= 1
            C -= 1
            
            sections = []
            
            # Top-left
            if R > 0 and C > 0:
                sections.append(min(a[i][j] for i in range(0,R) for j in range(0,C)))
            
            # Top-right
            if R > 0 and C < m-1:
                sections.append(min(a[i][j] for i in range(0,R) for j in range(C+1,m)))
            
            # Bottom-left
            if R < n-1 and C > 0:
                sections.append(min(a[i][j] for i in range(R+1,n) for j in range(0,C)))
            
            # Bottom-right
            if R < n-1 and C < m-1:
                sections.append(min(a[i][j] for i in range(R+1,n) for j in range(C+1,m)))
            
            ans.append(sum(sections))
        
        return ans
