class Solution:
    def climbStairs(self, n: int) -> int:
        twoAgo = 1 # this is just a special base case because soln[2] has to be 2
        oneAgo = 1

        for i in range(2, n+1):
            temp = twoAgo
            twoAgo = oneAgo
            oneAgo = oneAgo + temp
        
        return oneAgo