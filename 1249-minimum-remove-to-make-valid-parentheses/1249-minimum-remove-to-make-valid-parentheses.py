class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] # stores indices of opening or closing
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        
        s_list = list(s)
        # any indices left are unmatched parentheses
        for index in stack:
            s_list[index] = ""
            
        return "".join(s_list)