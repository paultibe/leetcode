from collections import defaultdict

class EquationNode:
    def __init__(self, numerator, denominator, ratioValue):
        self.numerator = numerator
        self.denominator = denominator
        self.ratioValue = ratioValue

    def __repr__(self):
        return f"({self.numerator}/{self.denominator} = {self.ratioValue})"

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        allEquationNodes = []
        allVariables = set()
        numeratorToNodesMap = defaultdict(list)
        adjacencyList = defaultdict(list)

        def buildGraph():
            for i, (numerator, denominator) in enumerate(equations):
                currentValue = values[i]
                
                forwardNode = EquationNode(numerator, denominator, currentValue)
                reciprocalNode = EquationNode(denominator, numerator, 1.0 / currentValue)
                
                allEquationNodes.extend([forwardNode, reciprocalNode])
                allVariables.update([numerator, denominator])
                
                numeratorToNodesMap[forwardNode.numerator].append(forwardNode)
                numeratorToNodesMap[reciprocalNode.numerator].append(reciprocalNode)
            
            for currentNode in allEquationNodes:
                if currentNode.denominator in numeratorToNodesMap:
                    adjacencyList[currentNode] = numeratorToNodesMap[currentNode.denominator]

        def dfs(currentNode, targetDenominator, visitedNodes):
            if currentNode.denominator == targetDenominator:
                return currentNode.ratioValue
            
            visitedNodes.add(currentNode)
            
            for neighborNode in adjacencyList[currentNode]:
                if neighborNode not in visitedNodes:
                    productOfRemainingPath = dfs(neighborNode, targetDenominator, visitedNodes)
                    if productOfRemainingPath != -1.0:
                        return currentNode.ratioValue * productOfRemainingPath
            return -1.0

        def processQueries():
            queryResults = []
            for queryNumerator, queryDenominator in queries:
                if queryNumerator not in allVariables or queryDenominator not in allVariables:
                    queryResults.append(-1.0)
                elif queryNumerator == queryDenominator:
                    queryResults.append(1.0)
                else:
                    wasFound = False
                    for startingNode in numeratorToNodesMap[queryNumerator]:
                        calculatedRatio = dfs(startingNode, queryDenominator, set())
                        if calculatedRatio != -1.0:
                            queryResults.append(calculatedRatio)
                            wasFound = True
                            break
                    if not wasFound:
                        queryResults.append(-1.0)
            return queryResults

        buildGraph()
        return processQueries()