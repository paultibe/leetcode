class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        scratch notes
        -if query[i][0] or query[i][1] not in equations, return -1
        searching for correct series of products of equations
        example input: [a/b, a/e, a/d, b/c, b/d, b/e, e/j] looking for: a/c
        a/b * b/c = a/c 
        a/a = 1
        first thought: 
        - model each node as the ratio where a neighbour exists if node1.denominator = node2.numerator
        - do multi-source dfs/bfs at each node where node.numerator = target.numerator
        - stop search when node.denominator = target.denominator
        - but what if you have input: [a/b, a/c] queries: [b/a, b/c]
        - so then you need to add an extra node for each input equation
        can model as a search in a graph where edge a -> b represents a/b
        need to start at first value in query, end at second

        - second thought
        - edges are transitions between nodes, thus each ratio can be an edge.
        - instead of adding two nodes for a/b and b/a, we add two edges to represent a -> b and b -> a
        - so if each equation becomes an edge, then when we traverse a -> b -> c, we want product of edges

        approach
        """
        # 1. Define our nodes and their base values
    # Each node is (numerator, denominator)
        node_values = {}
        adj = defaultdict(list)
        variables = set()

        for i, (num, den) in enumerate(equations):
            val = values[i]
            node_values[(num, den)] = val
            node_values[(den, num)] = 1.0 / val
            variables.add(num)
            variables.add(den)

        # 2. Build the adjacency list: Node A -> Node B
        # Connection exists if A.denominator == B.numerator
        all_nodes = list(node_values.keys())
        for i in range(len(all_nodes)):
            for j in range(len(all_nodes)):
                u_num, u_den = all_nodes[i]
                v_num, v_den = all_nodes[j]
                if u_den == v_num:
                    adj[all_nodes[i]].append(all_nodes[j])

        def dfs(curr_node, target_den, visited, current_product):
            if curr_node[1] == target_den:
                return current_product
            
            visited.add(curr_node)
            
            for neighbor in adj[curr_node]:
                if neighbor not in visited:
                    # Multiply by the value of the 'neighbor' equation node
                    result = dfs(neighbor, target_den, visited, current_product * node_values[neighbor])
                    if result != -1.0:
                        return result
            return -1.0

        results = []
        for C, D in queries:
            if C not in variables or D not in variables:
                results.append(-1.0)
                continue
            # Edge case: same variable
            # if C == D:
            #     results.append(1.0)
            #     continue
                
            found = False
            # multi-source
            for start_node in [n for n in all_nodes if n[0] == C]:
                res = dfs(start_node, D, set(), node_values[start_node])
                if res != -1.0:
                    results.append(res)
                    found = True
                    break
            
            if not found:
                results.append(-1.0)
                
        return results

        