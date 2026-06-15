# Max Area of Island
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = set()

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs_area(i, j):
            q = deque()
            q.append((i, j))
            visited.add((i, j))
            area = 0

            while q:
                x, y = q.popleft()
                area += 1

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < r
                        and 0 <= ny < c
                        and grid[nx][ny] == 1
                        and (nx, ny) not in visited
                    ):
                        q.append((nx, ny))
                        visited.add((nx, ny))
            
            return area

        max_area = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs_area(i, j))

        return max_area