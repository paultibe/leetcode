class Solution:
    def countAndSay(self, n: int) -> str:
        # Base Case
        if n == 1:
            return "1"
        
        # Recursive Step: Get the string from the previous step
        prev = self.countAndSay(n - 1)
        
        # Build the current string based on the previous result
        result = []
        i = 0
        while i < len(prev):
            count = 1
            # Count how many times the same character repeats
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                i += 1
                count += 1
            
            # Append "count" followed by "digit"
            result.append(str(count))
            result.append(prev[i])
            i += 1
            
        return "".join(result)