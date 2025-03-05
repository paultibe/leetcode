class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def filterString(string):
            stack1 = []
            for c in string:
                if c == "#":
                    if stack1:
                        stack1.pop()
                else:
                    stack1.append(c)
            return "".join(stack1)
        
        return filterString(s) == filterString(t)
        