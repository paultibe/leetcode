class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # countsS = Counter(s)
        counts = defaultdict(lambda: 0)
        for character in s:
            counts[character] += 1
        # countsT = Counter(t)
        for character in t:
            counts[character] -= 1

        for count in counts.values():
            if count != 0:
                return False
        return True