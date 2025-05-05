class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        original_val = grid[row][col]
        borders = []

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                r, c = queue.popleft()
                is_border = False

                # Also check if the start was on boundary
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    is_border = True
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols  and grid[nr][nc] != original_val:
                        is_border = True #starting point is border point
                    elif 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == original_val:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                if is_border:
                    borders.append((r, c))
        bfs(row, col)

        for r, c in borders: #color all the borders at the end
            grid[r][c] = color


        return grid