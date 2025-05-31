class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited, atlantic_visited = set(), set()
        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, visited):
            stack = []
            stack.append((r, c))
            visited.add((r, c))

            while stack:
                r, c = stack.pop()
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if (0 <= nr < rows) and (0 <= nc < cols) and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        stack.append((nr, nc))
                        visited.add((nr, nc))
                
        
        for j in range(cols):
            dfs(0, j, pacific_visited)
        for i in range(rows):
            dfs(i, 0, pacific_visited)
    
        for j in range(cols):
            dfs(rows-1, j, atlantic_visited)
        for i in range(rows):
            dfs(i, cols-1, atlantic_visited)

        return list(pacific_visited & atlantic_visited)