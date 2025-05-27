class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        '''
        def dfs(r, c, board, visited, word_ptr):
            visited.add((r, c))
            stack.append((r, c))
            Found = False 
            while stack:
                # end condition for recursion/backtracking\
                if word_ptr == len(word): #i.e all characters found
                    return True
                r, c = stack.pop()
                dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
                for i, j in dirs:
                    nr, nc = r + i, c + j
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == word[word_ptr] and (nr, nc) not in visited:
                            stack.append((nr, nc))
                            visited.add((nr, nc))
                            word_ptr += 1
                            Found = True
                if not Found:
                    #backtrack and start afresh 
                    # this is like tree pruning since the match is not found till now in the recursion, dont go this path
                    stack = []
                    visited = []
        '''


        # recursive dfs version
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c]
            ):
                return False
            
            temp = board[r][c]
            board[r][c] = "#"  # mark visited

            # Explore 4 directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            board[r][c] = temp  # backtrack
            return found



        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False # in case if dfs doesnt return true
                        


                        
        