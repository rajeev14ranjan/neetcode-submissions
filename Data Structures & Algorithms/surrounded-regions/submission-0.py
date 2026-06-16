# Surrounded Regions
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares or rectangles.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def multi_source_bfs(edgepoints):
            q = deque(edgepoints)

            while q:
                cx, cy = q.popleft()
                board[cx][cy] = "E"

                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy

                    if (
                        0 <= nx < R
                        and 0 <= ny < C
                        and board[nx][ny] == "O"
                    ):
                        q.append((nx, ny))
                        board[nx][ny] = "E"
            # end of multi_source_bfs

        # pacific
        edge_points = []

        for i in range(R):
            for j in range(C):
                if (i == 0 or j == 0 or i == R - 1 or j == C - 1) and board[i][j] == "O":
                    edge_points.append((i, j))

        # do a multi source bfs to find out points that are connects to Os on the edge, replace them with "E"
        multi_source_bfs(edge_points)

        # replace remaining "O -> "X" and "E" to "O"
        for i in range(R):
            for j in range(C):
                if board[i][j] == "E": board[i][j] = "O"
                elif board[i][j] == "O": board[i][j] = "X"
