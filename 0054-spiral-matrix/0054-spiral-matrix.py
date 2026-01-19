class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        
        # We need to keep track of visited cells without mutating the matrix
        # Using a set to track visited coordinates
        def solve(r, c, di, visited):
            # 1. VALIDATION: If out of bounds or visited, this path is empty
            if not (0 <= r < m and 0 <= c < n and (r, c) not in visited):
                return []

            # 2. ACTION: Add current cell to visited for this branch
            visited.add((r, c))
            current_val = [matrix[r][c]]
            
            # Directions: Right, Down, Left, Up
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            dr, dc = dirs[di]
            
            # 3. RECURSION: Try same direction first
            res = solve(r + dr, c + dc, di, visited)
            
            # 4. ROTATION: If same direction returned nothing, try rotating
            if not res:
                new_di = (di + 1) % 4
                new_dr, new_dc = dirs[new_di]
                res = solve(r + new_dr, c + new_dc, new_di, visited)
                
            # 5. RETURN: Current value + whatever the rest of the path found
            return current_val + res

        return solve(0, 0, 0, set())