class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        org_clr = image[sr][sc]
        rows, cols = len(image), len(image[0])

        def bfs(r,c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            image[r][c] = color  # Change the color     

            while queue:
                r, c = queue.popleft()
                dirs = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for (nr, nc) in dirs:  # <<< Use new variable names: nr, nc
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr, nc) not in visited and (image[nr][nc] == org_clr):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        image[nr][nc] = color  # Change the color     

        # call bfs only from starting point
        bfs(sr, sc)
        return image
        
        