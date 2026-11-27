class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        row_hashset = defaultdict(set)
        column_hashset = defaultdict(set)
        box_hashset = defaultdict(set)
        

        for row in range(0,9):
            for col in range(0,9):

                ele = board[row][col]

                if ele == ".":
                    continue
                
                box_key = (row//3, col//3)

                if (ele in row_hashset[row]) or (ele in      column_hashset[col]) or (ele in box_hashset[box_key]):
                    return False

                row_hashset[row].add(ele) 
                column_hashset[col].add(ele) 
                box_hashset[box_key].add(ele) 
        
        return True