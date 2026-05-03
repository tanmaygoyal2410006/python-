"""You are given an m x n integer matrix matrix with the following two properties:
• Each row is sorted in non-decreasing order You are given an m x n integer matrix matrix with the following two properties:
• Each row is sorted in non-decreasing order Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false"""
def searchMatrix(matrix, target):
    if not matrix:
        return False

    n, m = len(matrix), len(matrix[0])
    low, high = 0, n*m - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
