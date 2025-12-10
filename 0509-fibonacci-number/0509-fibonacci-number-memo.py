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

        def fibHelper(i):
            # base
            if i <= 1:
                return soln[i]
            # ask question
            if soln[i] != -1:
                return soln[i]

            soln[i] = fibHelper(i-1) + fibHelper(i-2)
            return soln[i]
        
        return fibHelper(n)
        