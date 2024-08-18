class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        v = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                v.append(matrix[i][j])
        v.sort()
        return v[k - 1]