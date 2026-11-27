class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rowhashset = defaultdict(list)
        columnhashset = defaultdict(list)
        boxhashset = defaultdict(list)

        for row in range(0,9):
            for col in range(0,9):

                ele = board[row][col]
                
                if ele == '.':
                    continue 

                if int(ele) > 9 or int(ele) < 1:
                    return False
                
                box = (row//3,col//3)

                if (ele in rowhashset[row]) or (ele in columnhashset[col]) or (ele in boxhashset[box]):
                    return False

                rowhashset[row].append(ele)
                columnhashset[col].append(ele)   
                boxhashset[box].append(ele)  

        return True  