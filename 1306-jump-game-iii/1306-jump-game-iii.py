class Solution:
    def canReach(self, arr, start):
        if arr[start] == 0:
            return True
        
        jump_value = arr[start]
        arr[start] = -1 
        
        for next_idx in (start + jump_value, start - jump_value):
            if 0 <= next_idx < len(arr) and arr[next_idx] >= 0:
                
                if self.canReach(arr, next_idx):
                    return True
                    
        return False