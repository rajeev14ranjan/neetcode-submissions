"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Clone Graph
# Given a node in a connected undirected graph, return a deep copy of the graph.

# Each node in the graph contains an integer value and a list of its neighbors.
# ******* Good Solution ********* useful later.


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        q = deque([node])
        oldtonew = {node: Node(node.val)}

        ans = None
        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in oldtonew:
                    q.append(nei)
                    oldtonew[nei] = Node(nei.val)

                oldtonew[curr].neighbors.append(oldtonew[nei])

        return oldtonew[node]
