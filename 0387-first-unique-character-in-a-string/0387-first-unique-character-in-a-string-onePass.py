class Solution:
    def firstUniqChar(self, s: str) -> int:
        # example: "statistics"
        # logic 
        counts = Counter(s) # works with any iterable
        # move unique values to hashset
        # uniqueLetters = set()
        # for letter, count in counts.items():
        #     if count == 1:
        #         uniqueLetters.add(letter)

        for i in range(len(s)):
            if s[i] in counts and counts[s[i]] == 1:
                return i

        # not found
        return - 1