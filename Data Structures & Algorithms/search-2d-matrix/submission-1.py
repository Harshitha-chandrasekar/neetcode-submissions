class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        l = 0
        r = len(matrix) - 1
        row = 0
        while l<=r:
            mid = l + ((r-l) // 2)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        # find col
        l = 0
        r = len(matrix[0]) - 1
        while l<=r:
            mid = l + ((r-l) // 2)
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False
        