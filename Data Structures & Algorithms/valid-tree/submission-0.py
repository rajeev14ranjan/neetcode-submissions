# Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# **************** DFS cycle detection ****************

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree with 'n' nodes MUST have exactly 'n - 1' edges
        if len(edges) != n - 1:
            return False

        # Build the adjacency list
        graph = {v: [] for v in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Stack stores tuples: (current_node, parent_node)
        stack = [(0, -1)]
        visited = set()

        while stack:
            u, parent = stack.pop()  # Standard list pop() works as a DFS stack

            if u in visited:
                return False  # Visited via a different path -> Cycle detected!

            visited.add(u)

            for v in graph[u]:
                if v == parent:
                    continue  # Properly skip the immediate parent edge

                if v not in visited:
                    stack.append((v, u))  # Push neighbor and mark 'u' as its parent

        # Verify that all nodes were reached (ensures the graph is fully connected)
        return len(visited) == n
