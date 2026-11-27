class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns =len(matrix[0])

        row_start, row_end = 0, rows-1
        final_row = -1

        while row_start <= row_end:

            mid = (row_start + row_end)//2

            if target >= matrix[mid][0] and target<= matrix[mid][columns-1]:
                final_row = mid
                break
            
            elif target < matrix[mid][0]:
                row_end = mid-1
            
            else:
                row_start = mid+1
        

        if final_row == -1:
            return False
        
        else:
            column_start, column_end = 0, columns-1

            while column_start <= column_end:

                mid = (column_start+column_end)//2

                if matrix[final_row][mid] == target:
                    return True
                
                elif matrix[final_row][mid] > target:
                    column_end =  mid-1
                else:
                    column_start = mid+1
        
        return False
