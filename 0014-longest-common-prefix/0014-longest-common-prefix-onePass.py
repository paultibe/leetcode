class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        # iterate through each word, then each letter 
        for i in range(len(strs[0])):
            letter = strs[0][i]  # use first string as reference
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != letter:
                    return result
            result += letter
        return result
        