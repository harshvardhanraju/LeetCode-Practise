class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        min_heap = [(0, (0,0))] #added startng node with 0 weight

        while min_heap:
            effort, (u, v) = heapq.heappop(min_heap)
            if u == rows - 1 and v == cols - 1:
                return effort
            dirs = [(u+1, v), (u-1, v), (u, v-1), (u, v+1)]
            for r, c in dirs:
                if 0 <= r < rows and 0 <= c < cols:
                    effort = abs(heights[u][v] - heights[r][c])
                    new_effort = max(dist[u][v], effort)
                    if dist[r][c] > new_effort:
                        dist[r][c] = new_effort
                        heapq.heappush(min_heap, (new_effort, (r, c)))
        
        return 0