class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        # Right, Down, Left, Up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, di):
            # 1. VALIDATION: Is this cell actually valid?
            if not (0 <= r < m and 0 <= c < n and matrix[r][c] is not None):
                return False # Signal that we hit a wall
            
            # 2. ACTION: Process the cell
            res.append(matrix[r][c])
            matrix[r][c] = None # Mark visited
            
            # 3. RECURSION: Try to continue in the SAME direction
            dr, dc = dirs[di]
            if not dfs(r + dr, c + dc, di):
                # 4. ROTATION: If current direction failed, try the NEXT one
                new_di = (di + 1) % 4
                new_dr, new_dc = dirs[new_di]
                dfs(r + new_dr, c + new_dc, new_di)
            
            return True

        dfs(0, 0, 0)
        return res