class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        island_existed = 0

        def bfs_max_area(r, c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            area = 1 #1st cell is counted by default

            while queue:
                val = queue.popleft()
                r, c = val
                dirs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for dir in dirs:
                    r, c = dir
                    if dir not in visited and (0<=r<rows and 0<=c<cols and grid[r][c] == 1):
                        queue.append((r, c))
                        visited.add((r, c))
                        area += 1                    
            return area
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = bfs_max_area(i, j)
                    max_area = max(area, max_area)
                    island_existed = 1
        
        # if not island_existed:
        #     return 0 #no islands
        
        return max_area
