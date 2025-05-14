import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for ip, op, cost in flights:
            graph[ip].append((op, cost)) #directed graph, so 1 side only

        
        min_heap = [(0, src, 0)] #cost, current point, total_stops
        dist = [float('inf')] * n
        dist[src] = 0

                
        # Track minimum stops taken to reach each city
        visited = dict()

        while min_heap:
            cost, city, stops = heapq.heappop(min_heap)

            if city == dst:
                return cost

            if stops > k:
                continue

            # Avoid revisiting nodes with more stops
            if (city in visited and visited[city] <= stops):
                continue
            visited[city] = stops

            for neighbor, price in graph[city]:
                heapq.heappush(min_heap, (cost + price, neighbor, stops + 1))

        return -1
            
            