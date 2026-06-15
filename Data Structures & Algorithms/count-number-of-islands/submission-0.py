class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])

        island = 0
        visited = set()

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                x, y = q.popleft()

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if (
                        0 <= nx < r
                        and 0 <= ny < c
                        and grid[nx][ny] == "1"
                        and (nx, ny) not in visited
                    ):
                        q.append((nx, ny))
                        visited.add((nx, ny))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island += 1
                    bfs(i, j)

        return island
