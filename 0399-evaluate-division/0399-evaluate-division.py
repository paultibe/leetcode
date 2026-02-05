class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        visited = set()

        def dfs(curr, target):
            nonlocal visited
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
            if q_src not in adj or q_target not in adj:
                results.append(-1.0)
                continue
            results.append(dfs(q_src, q_target))
            visited.clear()
            
        return results