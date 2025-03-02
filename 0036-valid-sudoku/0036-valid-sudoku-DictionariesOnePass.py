class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows
        # keep a hashset for each row
        BOARD_HEIGHT = 9
        BOARD_WIDTH = BOARD_HEIGHT
        SQUARE_HEIGHT = 3
        SQUARE_WIDTH = SQUARE_HEIGHT

        cols = defaultdict(set)
        rows =  defaultdict(set)
        squares = defaultdict(set)

        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_WIDTH):
                currentNumber = board[row][col]
                index = 3 * (row // 3) + col // 3
                if (currentNumber == "."):
                    continue
                if (currentNumber in rows[row]
                    or currentNumber in cols[col]
                    or currentNumber in squares[index]):
                    return False
                cols[col].add(currentNumber)
                rows[row].add(currentNumber)
                squares[index].add(currentNumber)
        
        return True