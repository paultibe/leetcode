class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        visited = set() # Define in parent scope

        def dfs(curr, target):
            if curr not in adj or target not in adj:
                return -1.0
            if curr == target:
                return 1.0

            visited.add(curr)

            for nei, weight in adj[curr]:
                if nei not in visited:
                    result = dfs(nei, target)
                    if result != -1.0:
                        return weight * result
            return -1.0

        results = []
        for q_src, q_target in queries:
            results.append(dfs(q_src, q_target))
            visited.clear() # Reuse the same memory
            
        return results