class Solution:
    def fib(self, n: int) -> int:
        # initialization is separate from recursion stuff.
        if n == 0:
            return 0
        if n == 1:
            return 1

        soln = [-1] * (n+1)
        soln[0] = 0
        soln[1] = 1

        for i in range (2, n+1):
            soln[i] = soln[i-1] + soln[i-2]
        
        return soln[n]
        