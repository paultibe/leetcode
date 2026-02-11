import collections

class MagicDictionary:
    def __init__(self):
        self.patterns = collections.defaultdict(int)

    def buildDict(self, words):
        self.words = set(words)
        for word in words:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:] # O(L)
                self.patterns[pattern] += 1

    def search(self, word):
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            count = self.patterns[pattern]
            
            if count > 1: # EDGE CASE
                return True
            if count == 1 and word not in self.words:
                return True
        return False