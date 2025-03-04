class Solution:
    def isValid(self, s: str) -> bool:
        bracketMappings = {")": "(", "]": "[", "}": "{"}
        stack = [] # LIFO
        # if open bracket, add to stack and move
        # if closed bracket, check that previous bracket is the corresponding one, then pop off stack
        for i in range(len(s)):
            if s[i] not in bracketMappings:
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    if stack[-1] != bracketMappings[s[i]]:
                        return False
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        