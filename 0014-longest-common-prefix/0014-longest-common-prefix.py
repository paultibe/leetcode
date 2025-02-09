class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(s) for s in strs]
        result = ""
        # iterate through each word, then each letter 
        for i in range(min(lengths)):
            letter = strs[0][i]  # use first string as reference
            for j in range(len(strs)):
                if strs[j][i] != letter:
                    return result
            result += letter
        return result
        