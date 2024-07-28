class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ar=[[0]*(len(board[0])+2)]
        for i in range(len(board)):
            l=[0]
            for j in range(len(board[0])):
                l.append(board[i][j])
            l.append(0)
            ar.append(l)    
        ar.append([0]*(len(board[0])+2))
        r,c=len(ar),len(ar[0])
        for i in range(1,r-1):
            for j in range(1,c-1):
                s=ar[i+1][j]+ar[i+1][j+1]+ar[i][j+1]+ar[i-1][j+1]+ar[i-1][j]+ar[i-1][j-1]+ar[i][j-1]+ar[i+1][j-1]
                if ar[i][j]==1 and s<2:
                    board[i-1][j-1]=0
                elif ar[i][j]==1 and s in [2,3]:
                    board[i-1][j-1]=1
                elif ar[i][j]==1 and s>3:
                    board[i-1][j-1]=0
                elif ar[i][j]==0 and s==3:
                    board[i-1][j-1]=1