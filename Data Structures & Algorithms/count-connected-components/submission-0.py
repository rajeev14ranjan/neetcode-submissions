# Number of Connected Components in an Undirected Graph
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.
# Return the number of connected components in the graph.


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # using union find ds since this is **undirected graph*** otherwise DFS
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y) -> bool:
            root_x, root_y = find(x), find(y)

            if root_x != root_y:
                parent[root_y] = root_x
                return True
            else:
                return False

        component_count = n  # at start there will be n components
        for u, v in edges:
            if union(u, v):
                component_count -= 1

        return component_count
