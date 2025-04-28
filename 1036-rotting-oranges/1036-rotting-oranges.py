class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # level_size = 0
        time = 0

        #bfs along with counting the levels of BFS
        visited = set()
        queue = deque()
        
        for i in range(rows):
            for j in range(cols): 
                if grid[i][j] == 2: # add all rotten in the queue to start with 
                    queue.append((i, j))
        
        dirs = [(1, 0), (-1, 0), (0, +1), (0, -1)]

        while queue:
            for _ in range(len(queue)): # run for loop for each level in the queue
                r, c = queue.popleft()

                for nr, nc in dirs:
                    nr, nc = r + nr, c + nc
                    if (nr, nc) not in visited and (0<=nr<rows) and (0<=nc<cols) and grid[nr][nc] == 1: #fresh
                        grid[nr][nc] = 2 #rotten the fresh one
                        queue.append((nr, nc))
            if len(queue) > 0: # if queue has new rotten tomatoes added, then add to time and proceed to next level
                time += 1
            
        for row in grid:
            if 1 in row: 
                return -1
    
        return time