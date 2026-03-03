class Solution:
    def validTicTacToe(self, board):
        # 1. Count pieces
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)
        
        # 2. Basic count pruning
        if o_count > x_count or x_count > o_count + 1:
            return False
        
        # Helper to check for a win
        def check_win(p):
            # Rows & Cols
            for i in range(3):
                if all(board[i][j] == p for j in range(3)): return True
                if all(board[j][i] == p for j in range(3)): return True
            # Diagonals
            if board[0][0] == board[1][1] == board[2][2] == p: return True
            if board[0][2] == board[1][1] == board[2][0] == p: return True
            return False

        x_wins = check_win('X')
        o_wins = check_win('O')
        
        # 3. Game State Pruning
        if x_wins and o_wins: return False # Both can't win
        if x_wins and x_count != o_count + 1: return False # X won, but O moved again
        if o_wins and x_count != o_count: return False # O won, but X moved again
        
        return True