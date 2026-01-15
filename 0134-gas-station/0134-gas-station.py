class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, end = n - 1, 0
        tank = gas[start] - cost[start]
        while start > end: # exit: moving of start accounts for station pointed to by start
            if tank < 0:
                start -= 1
                tank += gas[start] - cost[start] # move first. like recursive call without lookahead
            else:
                tank += gas[end] - cost[end]
                end += 1
        return start if tank >= 0 else -1