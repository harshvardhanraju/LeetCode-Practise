class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row, col =  len(board), len(board[0])
        visited = set()
        
        def bfs(r,c):
            isSurrounded = True
            component = [(r, c)]
            queue = deque() #new queue for every call
            queue.append((r,c))
            visited.add((r,c))


            while queue:
                ele = queue.popleft()
                r, c = ele
                if r==0 or r==row-1 or c==0 or c==col-1: #starting point is at boundary
                    isSurrounded = False
                for nr, nc in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                    if (0 <= nr < row) and (0 <= nc < col) and (board[nr][nc] == "O") and (nr, nc) not in visited :
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        component.append((nr, nc))

                    # if nr==0 or nr==row-1 or nc==0 or nc==col-1: #original point is at boundary
                    #     isSurrounded = False

            if isSurrounded: #if finally, after full bfs, its still surrounded, then capture it
                for x, y in component:
                    board[x][y] = "X"

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i, j) not in visited:
                    bfs(i, j)
        

        