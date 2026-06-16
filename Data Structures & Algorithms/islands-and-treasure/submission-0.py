class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        INF = 2147483647

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def multi_source_bfs(points):
            q = deque(points)
            visited = set(points)

            while q:
                cx, cy = q.popleft()

                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy

                    if (
                        0 <= nx < R
                        and 0 <= ny < C
                        and grid[nx][ny] == INF
                        and (nx, ny) not in visited
                    ):
                        q.append((nx, ny))
                        grid[nx][ny] = grid[cx][cy] + 1
                        visited.add((nx, ny))

        # call multisource bfs with all treasure points
        treasures = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    treasures.append((i, j))

        multi_source_bfs(treasures)
