class Solution:
    """
    # scratch notes
        # each minute, each rotten orange will rotten adjacent oranges
        # want to find how many waves of rottening to rotten all fruit
        # we can do a BFS with multi start nodes

        # plan:
        # iterate through grid and find all rotten fruit
        # do a BFS starting at each of those fruit. a cell is invalid (for BFS, so stop BFS) if  it's out of bounds, rotten, or empty
        # when BFS finishes, need to check if there are fruit remaining
        """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        numberOfRipeFruits = 0
        minimumMinutes = 0
        # clockwise from right
        toNeighbours = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
        queue = deque()

        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    numberOfRipeFruits += 1
        
        print(f"number of ripe fruits: {numberOfRipeFruits}")
        # bfs
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                # account for starting case
                if grid[row][col] == 1:
                    numberOfRipeFruits -= 1

                print(f"number of ripe fruits: {numberOfRipeFruits}")
                grid[row][col] = 2
                for toNextRow, toNextCol in toNeighbours:
                    newRow = row + toNextRow
                    newCol = col + toNextCol
                    if newRow < 0 or newCol < 0 or newRow >= ROWS or newCol >= COLUMNS or grid[newRow][newCol] != 1:
                        continue    
                    queue.append((newRow, newCol))
            # one wave of rottening
            if queue:
                minimumMinutes += 1
        
        # initial rotten fruits don't count
        return minimumMinutes if numberOfRipeFruits == 0 else -1




# post:
# BFS extends naturally to multiple sources.
# completely forgot about visited.
# input validation approach doesn't work because of starting condition: start with rotten oranges.
# thus have to adapt approach on the fly. that was always the point
# code ran forever: