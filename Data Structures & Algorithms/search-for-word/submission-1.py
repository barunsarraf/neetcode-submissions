class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        board_visited = [[0] * len(board[0]) for _ in range(len(board))]

        print(board_visited)
        def dfs(i,j,k,board_visited):

            if k==len(word):
                return True

            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board_visited[i][j] == 1 or board[i][j]!=word[k]:
                return False
            
            board_visited[i][j]=1

            found = (dfs(i+1,j,k+1,board_visited) or dfs(i-1,j,k+1,board_visited) or dfs(i,j+1,k+1,board_visited) or dfs(i,j-1,k+1,board_visited))
            
            board_visited[i][j] = 0

            return found

        def helper():

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if dfs(i,j,0,board_visited):
                        return True
            return False

        return helper()

