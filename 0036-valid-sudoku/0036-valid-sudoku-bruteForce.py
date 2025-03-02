class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        # keep a hashset for each row
        BOARD_HEIGHT = 9
        BOARD_WIDTH = BOARD_HEIGHT
        SQUARE_HEIGHT = 3
        SQUARE_WIDTH = SQUARE_HEIGHT
        for row in range(BOARD_HEIGHT):
            numbersSeenInRow = set()
            for col in range(BOARD_WIDTH):
                if board[row][col] == ".":
                    continue
                if board[row][col] in numbersSeenInRow:
                    return False
                numbersSeenInRow.add(board[row][col])
        # validate columns
        for col in range(BOARD_WIDTH):
            numbersSeenInCol = set()
            for row in range(BOARD_HEIGHT):
                if board[row][col] == ".":
                    continue
                if board[row][col] in numbersSeenInCol:
                    return False
                numbersSeenInCol.add(board[row][col])
                
        # validate 3x3 squares
        for square in range(BOARD_HEIGHT):
            numbersSeenInSquare = set()
            for i in range(SQUARE_HEIGHT):
                for j in range(SQUARE_WIDTH):
                    row = i + (SQUARE_HEIGHT * (square // 3))
                    col = j + (SQUARE_WIDTH * (square % 3))
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in numbersSeenInSquare:
                        return False
                    numbersSeenInSquare.add(board[row][col])
        
        # board is valid!
        return True
        # TODO: what if square is blank ("")
