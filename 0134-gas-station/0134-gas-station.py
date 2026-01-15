class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0
        end = 0
        tank = 0
        count = 0
        
        while count < n:
            net = gas[end] - cost[end]
            if tank + net >= 0:
                tank += net
                end += 1
            else:
                # Not enough gas? We must have started too late. 
                # Move start back and add its contribution.
                start = (start - 1 + n) % n
                tank += gas[start] - cost[start]
                
            count += 1
            
        return start if tank >= 0 else -1