"""Given a collection of candidate numbers (candidates) and a target number (target), find 
all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]"""
candidates = [10,1,2,7,6,1,5]
target = 8

candidates.sort()
result = []

def backtrack(start, path, total):
    if total == target:
        result.append(path)
        return
    
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i-1]:
            continue
        if total + candidates[i] > target:
            break
        
        backtrack(i+1, path+[candidates[i]], total+candidates[i])

backtrack(0, [], 0)

print(result)
