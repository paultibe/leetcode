class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCounts = Counter(magazine)

        for c in ransomNote:
            if c not in magCounts or magCounts[c] == 0:
                return False
            magCounts[c] -= 1
        return True