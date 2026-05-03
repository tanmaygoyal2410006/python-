"""Given a number x and an array of integers arr, find the smallest subarray with sum 
greater than the given value. If such a subarray do not exist return 0 in that case.
Examples:
Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
Output: 3
Explanation: Minimum length subarray is [4, 45, 6]
Input: x = 100, arr[] = [1, 10, 5, 2, 7]
Output: 0
Explanation: No subarray exist"""
def smallestSubarray(arr, x):
    n = len(arr)
    start = 0
    curr_sum = 0
    min_len = n + 1

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return 0 if min_len == n + 1 else min_len
