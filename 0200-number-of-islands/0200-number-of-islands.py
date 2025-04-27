from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col =  len(grid), len(grid[0])
        visited = set()
        islands = 0

        
        def bfs(r,c):
            queue = deque() #new queue for every call
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                ele = queue.popleft()
                r, c = ele
                for pair in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                    if (0 <= pair[0] < row) and (0 <= pair[1] < col) and (grid[pair[0]][pair[1]] == "1") and pair not in visited :
                        queue.append(pair)
                        visited.add(pair)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands


            
        