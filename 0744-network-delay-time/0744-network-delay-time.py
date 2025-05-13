import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # grid/graph matrix needs to be created
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n+1)
        dist[k] = 0
        min_heap = [(0, k)] #added startng node with 0 weight

        while min_heap:
            new_dist, u = heapq.heappop(min_heap)

            if new_dist > dist[u]: #skip and dont update
                continue
            for v, w in graph[u]:
                if dist[v] > dist[u] + w: #i.e older path was longer, then update to new
                    dist[v] = dist[u] + w
                    heapq.heappush(min_heap, (dist[v], v))
        
        if float("inf") in dist[1:]:
            return -1
        
        return max(dist[1:])
        