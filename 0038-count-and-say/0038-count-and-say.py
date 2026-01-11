class Solution:
    def countAndSay(self, n: int) -> str:
        stack = []
        # traverse down
        # a bit weird because each element on stack is just a value (not a node etc. )
        while n > 1:
            stack.append(n)
            n -= 1
        
        res = ["1"]
        
        while stack:
            stack.pop() # not even storing element
            
            next_term = []
            i = 0
            while i < len(res):
                count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    count += 1
                
                next_term.append(str(count))
                next_term.append(res[i])
                i += 1
            
            res = next_term
            
        return "".join(res)