"""Given an integer array nums of unique elements, return all possible subsets (the power 
set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
Input: nums = [0]
Output: [[],[0]]"""
nums = [1,2,3]

result = [[]]

for num in nums:
    new = []
    
    for subset in result:
        new.append(subset + [num])
    
    result = result + new

print(result)

