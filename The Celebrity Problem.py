class Solution:
    def celebrity(self, mat):
        if len(mat)==1:
            return 0
        top = 0
        down = len(mat)-1
        while down>top:
            if mat[down][top] == 1 and mat[top][down] == 1:
                top += 1
                down -= 1
            elif mat[down][top] == 1 and mat[top][down] == 0:
                down -= 1
            else:
                top += 1
        if top>down:
            return -1
        for i in range(len(mat)):
            if i==top:
                continue
            if mat[top][i]==0 and mat[i][top]==1:
                continue
            else:
                return -1
        return top