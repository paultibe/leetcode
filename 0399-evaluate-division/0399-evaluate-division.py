class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)  # Map a -> list of [b, a/b]

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, target):
            q, visit = deque([(src, 1)]), set()
            visit.add(src)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for nei, weight in adj[node]:
                    if nei not in visit:
                        visit.add(node)
                        q.append((nei, w * weight))
            return -1
        
        result = []
        for src, dest in queries:
            if src not in adj or dest not in adj:
                result.append(-1)
            else:
                result.append(bfs(src, dest))
    
        return result