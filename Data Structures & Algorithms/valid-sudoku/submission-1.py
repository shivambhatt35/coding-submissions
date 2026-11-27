class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        row_hashset = defaultdict(set)
        col_hashset = defaultdict(set)
        box_hashset = defaultdict(set)


        for row in range(0,9):
            for col in range(0,9):

                ele = board[row][col]

                if ele == ".":
                    continue
                
                box_row = (row//3, col//3)

                if (ele in row_hashset[row]) or (ele in col_hashset[col]) or (ele in box_hashset[box_row]):
                    return False
                
                row_hashset[row].add(ele)
                col_hashset[col].add(ele)
                box_hashset[box_row].add(ele)
        

        return True
        