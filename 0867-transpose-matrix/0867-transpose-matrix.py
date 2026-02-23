class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        new = []
        for col in range(COLS):
            col = []
            for row in range(ROWS):
                col.append(0)
            new.append(col)
        
        for row in range(ROWS):
            for col in range(COLS):
                new[col][row] = matrix[row][col]
        
        return new
