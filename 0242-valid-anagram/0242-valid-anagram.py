class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # countsS = Counter(s)
        countsS = {}
        for character in s:
            countsS[character] = countsS.get(character, 0) + 1
        # countsT = Counter(t)
        countsT = {}
        for character in t:
            countsT[character] = countsT.get(character, 0) + 1

        return countsS == countsT