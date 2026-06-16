# Course Schedule
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# The pair [0, 1], indicates that must take course 1 before taking course 0.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = {}
        graph = defaultdict(list)

        for v, u in prerequisites: # u ----> v
            degree[v] = degree.get(v, 0) + 1
            degree[u] = degree.get(u, 0)

            graph[u].append(v)

        zero_degree = [k for k, v in degree.items() if v == 0]

        queue = deque(zero_degree)

        topological = []

        while queue:
            u = queue.popleft()
            topological.append(u)

            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    queue.append(v)

        print(topological)
        return len(topological) == len(graph.keys())
