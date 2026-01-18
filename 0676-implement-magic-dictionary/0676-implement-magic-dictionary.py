import collections

class MagicDictionary:
    def __init__(self):
        self.patterns = collections.defaultdict(int)

    def buildDict(self, words):
        # We also need to store the actual words to handle 
        # the "exactly one" rule correctly.
        self.words = set(words)
        for word in words:
            for i in range(len(word)):
                # Create a pattern like "a*ple"
                pattern = word[:i] + "*" + word[i+1:]
                self.patterns[pattern] += 1

    def search(self, word):
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            count = self.patterns.get(pattern, 0)
            
            if count > 1:
                return True
            if count == 1 and word not in self.words:
                # If there's only one word matching this pattern, 
                # it MUST be a different word than our search word.
                return True
        return False