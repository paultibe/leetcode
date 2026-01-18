class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, words):
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

    def search(self, word):
        # Helper function for DFS search
        def dfs(node, index, modified):
            if index == len(word):
                # We must have modified exactly one char AND be at the end of a word
                return modified and node.is_end
            
            char = word[index]
            
            # Option 1: The characters match
            if char in node.children:
                if dfs(node.children[char], index + 1, modified):
                    return True
            
            # Option 2: The characters don't match (only if we haven't modified yet)
            if not modified:
                for next_char in node.children:
                    if next_char != char: # Try every branch except the "correct" one
                        if dfs(node.children[next_char], index + 1, True):
                            return True
            
            return False

        return dfs(self.root, 0, False)