from collections import deque
class Solution:
    def is_inside(self, x, y, N):
        return 1 <= x <= N and 1 <= y <= N
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        queue = deque([(KnightPos[0], KnightPos[1], 0)])
        visited = set((KnightPos[0], KnightPos[1]))
        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == (TargetPos[0], TargetPos[1]):
                return steps
            for move in moves:
                new_x, new_y = x + move[0], y + move[1]
                
                if self.is_inside(new_x, new_y, N) and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, steps + 1))
                    visited.add((new_x, new_y))
        return -1