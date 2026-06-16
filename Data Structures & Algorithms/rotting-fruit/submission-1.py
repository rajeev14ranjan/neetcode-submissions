# Rotting Fruit
# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def multi_source_bfs(points, fresh_fruit_count):
            q = deque(points)

            time = 0
            while q:
                for _ in range(len(q)):
                    cx, cy = q.popleft()

                    for dx, dy in dirs:
                        nx, ny = cx + dx, cy + dy

                        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                            q.append((nx, ny))
                            grid[nx][ny] = 2  # mark as rotten
                            fresh_fruit_count -= 1

                time += 1
                if fresh_fruit_count <= 0:
                    return time

        # call multisource bfs with all treasure points
        rotten_fruits = []
        fresh_fruit_count = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    rotten_fruits.append((i, j))
                elif grid[i][j] == 1:
                    fresh_fruit_count += 1

        if not fresh_fruit_count: return 0
        time = multi_source_bfs(rotten_fruits, fresh_fruit_count)
        return time or -1
