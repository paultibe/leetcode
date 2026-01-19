class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        
        # clockwise
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, di):
            if len(res) == m * n:
                return
            
            res.append(matrix[r][c])
            matrix[r][c] = "#"
            
            # try
            dr, dc = dirs[di]
            next_r, next_c = r + dr, c + dc
            
            # if next not valid, rotate
            if not (0 <= next_r < m and 0 <= next_c < n and matrix[next_r][next_c] is not "#"):
                di = (di + 1) % 4
                dr, dc = dirs[di]
                next_r, next_c = r + dr, c + dc
            
            dfs(next_r, next_c, di)

        dfs(0, 0, 0)
        return res