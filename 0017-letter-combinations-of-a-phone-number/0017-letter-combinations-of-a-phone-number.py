class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = ""
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            nonlocal path
            if i == len(digits):
                res.append(path)
                return
            for c in digitToChar[digits[i]]:
                path = path + c
                backtrack(i + 1)
                path = path[:len(path) - 1]

        if digits:
            backtrack(0)

        return res