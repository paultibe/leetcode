import collections

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        adjacencyList = collections.defaultdict(list)
        for i, (numerator, denominator) in enumerate(equations):
            adjacencyList[numerator].append((denominator, values[i]))
            adjacencyList[denominator].append((numerator, 1 / values[i]))

        visitedNodes = set()

        def dfs(currentNode, targetNode, currentProduct):
            if currentNode == targetNode:
                return currentProduct

            visitedNodes.add(currentNode)

            for neighborNode, edgeWeight in adjacencyList[currentNode]:
                if neighborNode not in visitedNodes:
                    # do computation before recursion!
                    result = dfs(neighborNode, targetNode, currentProduct * edgeWeight)
                    if result != -1.0:
                        return result
            return -1.0

        results = []
        for querySource, queryTarget in queries:
            if querySource not in adjacencyList or queryTarget not in adjacencyList:
                results.append(-1.0)
                continue
            
            results.append(dfs(querySource, queryTarget, 1.0))
            visitedNodes.clear()
            
        return results