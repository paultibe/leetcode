class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # 1. Pre-allocate the matrix with 0s (no list comprehension)
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            matrix.append(row)
        
        # Clockwise directions: Right, Down, Left, Up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # We start with the number 1
        def dfs(r, c, di, current_val):
            # Base Case: We have filled all n^2 cells
            if current_val > n * n:
                return
            
            # Fill the current cell
            matrix[r][c] = current_val
            
            # Lookahead to find the next cell
            dr, dc = dirs[di]
            next_r, next_c = r + dr, c + dc
            
            # If next is out of bounds or already filled (!= 0), rotate
            if not (0 <= next_r < n and 0 <= next_c < n and matrix[next_r][next_c] == 0):
                di = (di + 1) % 4
                dr, dc = dirs[di]
                next_r, next_c = r + dr, c + dc
            
            # Recurse with the next value
            dfs(next_r, next_c, di, current_val + 1)

        dfs(0, 0, 0, 1)
        return matrix