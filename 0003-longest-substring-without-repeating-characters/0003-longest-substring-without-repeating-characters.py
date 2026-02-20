class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        approach:
        - scan array with two pointers
        - expand window while element at right not in set, adding to set while expanding
        - if element at right in set, shrink window while popping from set
        - keep track of maxLength and currentLength (can possibly optimize)
        """
        maxLength = 0
        left, right = 0, 0
        charactersInWindow = set()
        for i in range(len(s)):
            if s[i] not in charactersInWindow:
                charactersInWindow.add(s[i])
                right += 1
                maxLength = max(maxLength, right - left)
                print(charactersInWindow)
            else:
                while s[i] in charactersInWindow:
                    charactersInWindow.remove(s[left])
                    left += 1
                charactersInWindow.add(s[i])
                right += 1
                print(charactersInWindow)
        return maxLength
        