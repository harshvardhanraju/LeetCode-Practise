# from collections import deque
# class Solution:
#     def closedIsland(self, grid: List[List[int]]) -> int:
#         visited = set()
#         count = 0
#         def bfs(r, c):
#             queue = deque()
#             queue.append((r, c))
#             visited.add((r, c))
#             isClosed = True
#             while queue:
#                 r, c = queue.popleft()
#                 dirs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
#                 for nr, nc in dirs:
#                     if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
#                         if nr==0 or nr==rows-1 or nc==0 or nc==cols-1:
#                             isClosed = False
#                         queue.append((nr, nc))
#                         visited.add((nr, nc))
#             return isClosed

#         rows, cols = len(grid), len(grid[0])
#         # for i in range(rows):
#         #     for j in range(cols):
#         #         if grid[i][j] == 1:
#         #             visited.add((i, j))
#         #         elif grid[i][j] == 0 and (i, j) not in visited:
#         #             if i==0 or i==rows-1 or j==0 or j==cols-1: #0 in boundary, so not island
#         #                 visited.add((i, j))
#         #             else:
#         #                 isIsland = bfs(i, j) # count
#         #                 if isIsland:
#         #                     count += 1
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == 0 and (i, j) not in visited:
#                     if bfs(i, j):
#                         count += 1
#         return count 

from collections import deque
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            isClosed = True
            while queue:
                r, c = queue.popleft()
                # Also check if the start was on boundary
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    isClosed = False
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                        if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                            isClosed = False
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            return isClosed

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if bfs(i, j):
                        count += 1

        return count
           


        