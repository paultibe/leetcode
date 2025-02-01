class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # not allowed:
        # e -> d
        # g -> d
        
        # scratch notes
        # e -> a
        # g -> d
        # g -> d
        # must have 1 to 1 mapping between characters 

        # time: O(n)
        # space: O(n)
        if len(s) != len(t):
            return False
        mappingsForS = {}
        tCharacters = set()
        for i in range(len(s)):
            # characters in S map to the same character in T
            print(f"current index: {i}")
            if s[i] in mappingsForS:
                if t[i] != mappingsForS[s[i]]:
                    return False
            if s[i] not in mappingsForS and t[i] in tCharacters:
                return False
            tCharacters.add(t[i])
            mappingsForS[s[i]] = t[i]
        
        return True


        