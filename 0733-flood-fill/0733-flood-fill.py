class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingCell = (sr, sc)
        # clockwise, top, right, bottom, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        NUM_ROWS = len(image)
        NUM_COLS = len(image[0])
        visited = set()

        def dfs(cell):
            row, col = cell
            image[row][col] = color
            visited.add(cell)
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if (newRow >= 0 
                    and newRow < NUM_ROWS
                    and newCol >= 0
                    and newCol < NUM_COLS
                    and image[newRow][newCol] == originalColor
                    and (newRow, newCol) not in visited):
                    # go there
                    dfs((newRow, newCol))

        originalColor = image[sr][sc]
        dfs((sr, sc))
        return image
        