class Solution:
    def shortest_distance(self, matrix):
        m=len(matrix)
        for i in range(m):
            for j in range(m):
                if matrix[i][j]==-1:
                    matrix[i][j]=float('inf')
                
        for i in range(m):
            for j in range(m):
                for k in range(m):
                    if matrix[j][i]+matrix[i][k]<matrix[j][k]:
                        matrix[j][k]=matrix[j][i]+matrix[i][k]
                       
        for i in range(m):
            for j in range(m):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=-1
        return matrix