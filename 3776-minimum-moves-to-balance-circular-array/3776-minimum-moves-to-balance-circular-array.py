class Solution:
    def minMoves(self, balance):
        n = len(balance)
        total_sum = sum(balance)
        
        # If the total is negative, we can't make everyone non-negative
        if total_sum < 0:
            return -1
            
        neg_idx = -1
        for i in range(n):
            if balance[i] < 0:
                neg_idx = i
                break
                
        # If no one is negative, 0 moves needed
        if neg_idx == -1:
            return 0
            
        debt = abs(balance[neg_idx])
        sources = []
        
        for i in range(n):
            if balance[i] > 0:
                # Calculate shortest distance in a circular array
                dist = min(abs(i - neg_idx), n - abs(i - neg_idx)) # IMPORTANT SECOND PART
                sources.append((dist, balance[i]))
                
        # Sort sources by distance (closest first)
        sources.sort()
        
        total_moves = 0
        for dist, amount in sources:
            if debt <= 0:
                break
            
            take = min(debt, amount) # IMPORTANT
            total_moves += take * dist # ALSO IMPORTANT
            debt -= take
            
        return total_moves