class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache
        def dfs(i):
            # have a unique decoded string
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            decodeUsingOneDigit = dfs(i + 1)
            decodeUsingTwoDigits = 0
            if i < len(s) - 1:
                if (s[i] == '1' or
                   (s[i] == '2' and s[i + 1] < '7')):
                    decodeUsingTwoDigits = dfs(i + 2)

            return decodeUsingOneDigit + decodeUsingTwoDigits

        return dfs(0)