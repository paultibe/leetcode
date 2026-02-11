class MagicDictionary:
    def __init__(self):
        self.words = []

    def buildDict(self, words: list[str]) -> None:
        # Just store the reference. O(1) or O(N) if copying.
        self.words = words

    def search(self, searchWord: str) -> bool:
        L = len(searchWord)
        
        for word in self.words:
            # Step 1: Length must match exactly
            if len(word) != L:
                continue
            
            # Step 2: Count mismatches
            mismatches = 0
            for i in range(L):
                if word[i] != searchWord[i]:
                    mismatches += 1
                
                # Optimization: stop early if we find too many diffs
                if mismatches > 1:
                    break
            
            # Step 3: Check "exactly one" rule
            if mismatches == 1:
                return True
                
        return False