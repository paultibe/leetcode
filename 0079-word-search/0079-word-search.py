class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        scratch notes
        - keep a visited set FOR CURRENT PATH
        - can do dfs and bfs i think. will do dfs. so lazy marking
        - base case is i == len(word). if we reached here, we know we found word.
        - need to backtrack if path didn't work out. 
        - how do we maintain what letter we're looking for -> where we are in the target word
        - just index? if index, then backtracking can be embedded within recursion
        - popping off call stack decrements index
        - start top left (0, 0), index 0
        '''
        ROWS, COLUMNS = len(board), len(board[0])
        # clockwise from right
        toNext = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        visited = set()

        def dfs(row, column, index):
            if board[row][column] == word[index]:
                index += 1
                visited.add((row, column)) # lazy marking
                if index == len(word):
                    visited.remove((row, column))
                    return True
            else:
                return False
            
            # recursive calls
            for toNextRow, toNextColumn in toNext:
                nextRow = row + toNextRow
                nextColumn = column + toNextColumn
                # lookahead
                outOfBounds = (min(nextRow, nextColumn) < 0) or (nextRow >= ROWS) or (nextColumn >= COLUMNS)
                if outOfBounds or (nextRow, nextColumn) in visited:
                    continue
                if dfs(nextRow, nextColumn, index): 
                    return True
            
            visited.remove((row, column))
            return False
        
        for row in range(ROWS):
            for col in range(COLUMNS):
                if dfs(row, col, 0):
                    return True
        
        return False
"""
retro
outOfBounds has to be first, otherwise you get indexing error
easy to forget backtracking or get it wrong. current function should handle its own backtracking
(!) if current cell doesn't match corresponding letter in word, have to exit
- even if you might encounter the correct next letter later on, correct future cells may already be in visited
can't start just at top left. if you do, by the time you reach the correct first cell, the correct future cells may already be in visited.
"""