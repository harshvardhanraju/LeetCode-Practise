import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        

        # grid/graph matrix needs to be created
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))  # undirected

        dist = [0.0] * (n+1)
        dist[start_node] = 1.0
        max_heap = [(-1.0, start_node)] #added startng node with 0 weight

        while max_heap:
            curr_prob, u = heapq.heappop(max_heap)
            curr_prob = - curr_prob #going back to actual prob values as we negated them earlier
            if u == end_node:
                return curr_prob

            for v, prob in graph[u]:
                if dist[v] < dist[u] * prob: #i.e older path was longer, then update to new
                    dist[v] = dist[u] * prob
                    heapq.heappush(max_heap, (-dist[v], v))
        
        
        return 0