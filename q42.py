"""Given an array nums of n integers, return an array of all 
the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
• 0 <= a, b, c, d < n
• a, b, c, and d are distinct.
• nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0 Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]"""
nums = [1,0,-1,0,-2,2]
target = 0

nums.sort()
result = []

n = len(nums)

for i in range(n):
    for j in range(i+1, n):
        left = j+1
        right = n-1
        
        while left < right:
            total = nums[i]+nums[j]+nums[left]+nums[right]
            
            if total == target:
                result.append([nums[i],nums[j],nums[left],nums[right]])
                left += 1
                right -= 1
            
            elif total < target:
                left += 1
            else:
                right -= 1

print(result)
