class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # just delimiter doesn't work
        # neet,code,love,you
        # just length doesn't work
        # 4neet4code4love3you15areallylongword
        # combine
        # 4#need4#code15#areallylongword
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result
        # TODO with list
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # 4#need4#code15#areallylongword
        result = []
        i = 0
        while i < len(s): # while loop because custom increments
            length = ""
            while s[i] != "#": # might be better to use j for clarity
                length += s[i]
                i += 1
            print(length)
            i += 1
            result.append(s[i:i + int(length)])
            i += int(length)
        
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))