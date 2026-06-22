class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {i: set() for i in range(9)}
        column_map = {i: set() for i in range(9)}
        sub_box_map = {i: set() for i in range(9)}

        for row_inx in range(0, 9):
                for clm_inx in range(0, 9):
                        if board[row_inx][clm_inx] == '.':
                                continue

                        if board[row_inx][clm_inx] in row_map[row_inx]:
                                return False        
                        row_map[row_inx].add(board[row_inx][clm_inx])

                        if board[row_inx][clm_inx] in column_map[clm_inx]:
                                return False
                        column_map[clm_inx].add(board[row_inx][clm_inx])
                        
                        sub_box_inx = (row_inx // 3) * 3  + clm_inx // 3
                        if board[row_inx][clm_inx] in sub_box_map[sub_box_inx]:
                                return False
                        sub_box_map[sub_box_inx].add(board[row_inx][clm_inx])
        
        return True
                