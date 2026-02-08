class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            # cycle
            if crs in visiting:
                return False
            # no prereqs
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            while preMap[crs]:
                pre = preMap[crs][-1] # Peek at the last element
                if not dfs(pre):      # If ANY child fails, return False immediately
                    return False
                preMap[crs].pop()
            visiting.remove(crs)
            return preMap[crs] == []

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True