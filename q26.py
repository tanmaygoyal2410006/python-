"""Given an array arr[] of integers, calculate the median.
Examples:
Input: arr[] = [90, 100, 78, 89, 67]
Output: 89
Explanation: After sorting the array middle element is the median 
Input: arr[] = [56, 67, 30, 79]
Output: 61.5
Explanation: In case of even number of elements, average of two middle elements is 
the median. 
Input: arr[] = [1, 2]
Output: 1.5
Explanation: The average of both elements will result in 1.5."""
def findMedian(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n//2 - 1] + arr[n//2]) / 2
