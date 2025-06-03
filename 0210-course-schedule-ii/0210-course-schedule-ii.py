from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #dfs based approach 
        
        #build adjcacency or dependency matrix
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[y].append(x)

        visited = [0] * numCourses  # keep 3 states for every node, 0: not visited, 1: visitin, 2:visited
        stack = []
        def dfs(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return 
            visited[node] = 1 # make the node as 'visiting'
            for neighbour in graph[node]:
                if dfs(neighbour):
                    return True
            visited[node] = 2 # make the node as 'visited'after dfs calls returns back
            stack.append(node)
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i):
                    return []
        return stack[::-1] # if no cyles, return reversed stack



        