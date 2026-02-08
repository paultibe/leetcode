class Solution:
    def numDecodings(self, s: str) -> int:

        cache = {}
        for i in range(len(s), -1, -1):
            if i == len(s):
                cache[i] = 1
                continue
            if s[i] == '0':
                cache[i] = 0
                continue
            
            decodeUsingOneDigit = cache[i + 1]
            decodeUsingTwoDigits = 0
            if i < len(s) - 1:
                if (s[i] == '1' or
                   (s[i] == '2' and s[i + 1] < '7')):
                    decodeUsingTwoDigits = cache[i + 2]

            cache[i] = decodeUsingOneDigit + decodeUsingTwoDigits

        return cache[0]