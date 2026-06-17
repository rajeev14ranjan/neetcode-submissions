# Redundant Connection
# You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.
# We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]  # nodes are 1-indexed

        def find(x) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            rootx, rooty = find(x), find(y)

            if rootx == rooty:
                return False

            parent[rooty] = rootx
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
