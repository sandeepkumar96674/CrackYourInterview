from typing import List
from typing import List

class Solution:
    def sumZeroMatrix(self, matrix : List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return 0, []

        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        max_rect = []
    
        for left in range(cols):
            row_sum = [0] * rows
            for right in range(left, cols):
                for row in range(rows):
                    row_sum[row] += matrix[row][right]
    
                current_sum = 0
                sum_map = {0: -1}
                for i in range(rows):
                    current_sum += row_sum[i]
                    if current_sum in sum_map:
                        area = (right - left + 1) * (i - sum_map[current_sum])
                        if area > max_area:
                            max_area = area
                            max_rect = [sum_map[current_sum] + 1, left, i, right]
                    else:
                        sum_map[current_sum] = i
    
        res = []
        for row in range(max_rect[0], max_rect[2] + 1):
            res.append(matrix[row][max_rect[1]:max_rect[3] + 1])
    
        return res