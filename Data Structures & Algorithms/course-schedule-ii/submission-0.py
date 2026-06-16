# Course Schedule II
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = {}
        graph = {}

        for course in range(numCourses):
            degree[course] = 0
            graph[course] = []

        for a, b in prerequisites:  # b ----> a
            degree[a] = degree.get(a, 0) + 1
            graph[b].append(a)

        zero_in_degree = [k for k, d in degree.items() if d == 0]

        queue = deque(zero_in_degree)

        topological = []

        while queue:
            u = queue.popleft()
            topological.append(u)

            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 0:
                    queue.append(v)

        return topological if len(topological) == numCourses else []
