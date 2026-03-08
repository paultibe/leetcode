class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []

        def dfs(start, end):
            if end >= len(s):
                if end == start: # we just added a palindromic substring to our path
                    res.append(path.copy())
                return

            if self.isPali(s, start, end):
                path.append(s[start : end + 1]) # take
                dfs(end + 1, end + 1) # break
                path.pop()

            dfs(start, end + 1) # extend

        dfs(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True