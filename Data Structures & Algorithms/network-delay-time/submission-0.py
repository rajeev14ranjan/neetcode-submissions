# Network Delay Time
# You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

# ui is the source node (an integer from 1 to n)
# vi is the target node (an integer from 1 to n)
# ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
# You are also given an integer k, representing the node that we will send a signal from.

# Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.
# ************** Dijkstra's algorithm ****************

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n+1)}

        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        
        distance = [math.inf] * (n + 1)
        visited = set()

        # start with k node
        distance[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            currdist, currnode = heapq.heappop(min_heap)

            if currnode in visited: continue
            visited.add(currnode)

            for nei, weight in graph[currnode]:
                newdistfornei = currdist + weight
                if newdistfornei < distance[nei]:
                    distance[nei] = newdistfornei
                    heapq.heappush(min_heap, (newdistfornei, nei))
        
        ans = -1
        for d in distance[1:]:
            if d == math.inf: return -1
            ans = max(ans, d)

        return ans

















