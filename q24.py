"""Given an array arr and a number k. One can apply a swap operation on the array any 
number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find 
the minimum number of swaps required to bring all the numbers less than or equal 
to k together, i.e. make them a contiguous subarray.
Examples :
Input: arr[] = [2, 1, 5, 6, 3], k = 3
Output: 1
Explanation: To bring elements 2, 1, 3 together, swap index 2 with 4 (0-based 
indexing), i.e. element arr[2] = 5 with arr[4] = 3 such that final array will be- arr[] = [2, 
1, 3, 6, 5]
Input: arr[] = [2, 7, 9, 5, 8, 7, 4], k = 6 
Output: 2 
Explanation: To bring elements 2, 5, 4 together, swap index 0 with 2 (0-based 
indexing) and index 4 with 6 (0-based indexing) such that final array will be- arr[] = 
[9, 7, 2, 5, 4, 7, 8]
Input: arr[] = [2, 4, 5, 3, 6, 1, 8], k = 6 
Output: 0"""
def minSwaps(arr, k):
    n = len(arr)
    count = 0

    for x in arr:
        if x <= k:
            count += 1

    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1

    ans = bad
    i = 0

    for j in range(count, n):
        if arr[j] > k:
            bad += 1
        if arr[i] > k:
            bad -= 1
        ans = min(ans, bad)
        i += 1

    return ans
