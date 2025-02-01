class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        myMap = {}
        mySet = set()
        first = 0
        second = 0

        while first < len(s):
            if s[first] in myMap:
                # two characters map to same character
                if t[second] != myMap[s[first]]:
                    return False
                # otherwise, keep moving
            else:
                # has already been mapped to
                if t[second] in mySet: return False
                # create mapping
                myMap[s[first]] = t[second]
                mySet.add(t[second])
                print(f"creating mapping from {s[first]} to {t[second]}")
            first += 1
            second += 1

        return True