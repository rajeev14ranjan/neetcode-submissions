# Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# **************** UNION FIND ****************


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1 : return False # more than n-1 edges will lead to cycle among n nodes.

        parent = [i for i in range(n)]  # using union-find/disjont-set data structure
        sets_count = n # all elements are set in themselves

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal sets_count
            par_x = find(x)
            par_y = find(y)

            if par_x != par_y:
                parent[par_y] = par_x
                sets_count -= 1

        for u, v in edges:
            if find(u) == find(v):
                return False  # edge between same set, trees can't have cycle

            union(u, v)

        # only return true if all the nodes are connected, i.e there is only 1 set at the end
        # trees can't have cycle, they also can't have disconnected node.
        return sets_count == 1 
