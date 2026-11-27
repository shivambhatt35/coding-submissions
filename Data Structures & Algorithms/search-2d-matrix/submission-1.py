class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix)-1, len(matrix[0])-1

        left, right = 0, rows
        our_row = -1

        while left<=right:

            mid = (left+right)//2

            if matrix[mid][0]<=target and matrix[mid][cols]>= target:
                our_row = mid
                break
            
            elif matrix[mid][cols]< target:
                left = mid+1
            
            else:
                right = mid-1
        
        if our_row == -1:
            return False
        
        left_col, right_col = 0, cols

        while left_col <= right_col:

            mid = (left_col+right_col)//2

            if matrix[our_row][mid] == target:
                return True

            elif matrix[our_row][mid] > target:
                right_col = mid-1
            
            else:
                left_col = mid+1
        
        return False



        