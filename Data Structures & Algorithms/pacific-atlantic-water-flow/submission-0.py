# Pacific Atlantic Water Flow
# You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def multi_source_bfs(visited):
            q = deque(list(visited))

            while q:
                cx, cy = q.popleft()

                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy

                    if (
                        0 <= nx < R
                        and 0 <= ny < C
                        and (nx, ny) not in visited
                        and heights[nx][ny] >= heights[cx][cy]
                    ):
                        q.append((nx, ny))
                        visited.add((nx, ny))
            # end of multi_source_bfs

        # pacific
        pacific_points = set()
        atlantic_points = set()

        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0:
                    pacific_points.add((i, j))

                if i == R - 1 or j == C - 1:
                    atlantic_points.add((i, j))

        # do a multi source bfs to find out points that can be climbed up to from ocean => water can flow down from those points back ocean
        multi_source_bfs(pacific_points)
        multi_source_bfs(atlantic_points)

        # return the intersection of cells visited by both pacific and altantic ocean
        ans_set = pacific_points & atlantic_points
        return list(map(list, ans_set))
