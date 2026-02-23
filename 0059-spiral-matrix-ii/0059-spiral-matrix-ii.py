class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            matrix.append(row)
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c, di, current_val):
            if current_val > n * n:
                return
            
            matrix[r][c] = current_val
            
            dr, dc = dirs[di]
            next_r, next_c = r + dr, c + dc
            
            if not (0 <= next_r < n and 0 <= next_c < n and matrix[next_r][next_c] == 0):
                di = (di + 1) % 4
                dr, dc = dirs[di]
                next_r, next_c = r + dr, c + dc
            
            dfs(next_r, next_c, di, current_val + 1)

        dfs(0, 0, 0, 1)
        return matrix