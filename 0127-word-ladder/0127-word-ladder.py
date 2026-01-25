class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        n, lengthOfEachWord = len(wordList), len(wordList[0])
        neighboursOf = defaultdict(list)
        mp = {}
        for i in range(n):
            mp[wordList[i]] = i

        # for every pair of words, if they differ by 1, add an edge
        for i in range(n):
            for j in range(i + 1, n):
                numberOfDifferences = 0
                for character in range(lengthOfEachWord):
                    if wordList[i][character] != wordList[j][character]:
                        numberOfDifferences += 1
                if numberOfDifferences == 1:
                    neighboursOf[i].append(j)
                    neighboursOf[j].append(i)

        q, res = deque(), 1
        visit = set()
        for i in range(lengthOfEachWord):
            for c in range(97, 123):
                if chr(c) == beginWord[i]:
                    continue
                # try inserting the character you're changing at every slot
                word = beginWord[:i] + chr(c) + beginWord[i + 1:]
                if word in mp and mp[word] not in visit:
                    q.append(mp[word])
                    visit.add(mp[word]) # eager marking

        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res
                for nei in neighboursOf[node]:
                    if nei not in visit: # lookahead
                        visit.add(nei) # eager marking
                        q.append(nei)

        return 0