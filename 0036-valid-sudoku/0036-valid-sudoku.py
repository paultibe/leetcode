class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # BRUTE FORCE
        ROWS = 9
        COLS = 9
        SUBBOX_SIZE = 3
        SUBBOX_PER_ROW = ROWS // SUBBOX_SIZE
        SUBBOX_PER_COL = COLS // SUBBOX_SIZE
        

        # validate rows
        for row in range(ROWS):
            seen = set()
            for col in range(COLS):
                if board[row][col] in seen:
                    return False
                if board[row][col] != ".":
                        seen.add(board[row][col])

        # validate cols
        for col in range(COLS):
            seen = set()
            for row in range(ROWS):
                if board[row][col] in seen:
                    return False
                if board[row][col] != ".":
                        seen.add(board[row][col])
        
        def isValidSubbox(topLeftRow, topLeftCol):
            seen = set()
            for row in range(topLeftRow, topLeftRow + SUBBOX_SIZE):
                for col in range(topLeftCol, topLeftCol + SUBBOX_SIZE):
                    if board[row][col] in seen:
                        return False
                    if board[row][col] != ".":
                        seen.add(board[row][col])
            return True

        # validate subgrids
        # 0,0 0,3 0,6
        for i in range(SUBBOX_PER_ROW):
            for j in range(SUBBOX_PER_COL):
                topLeftRow = i * 3
                topLeftCol = j * 3
                if not isValidSubbox(topLeftRow, topLeftCol):
                    return False
        
        return True

