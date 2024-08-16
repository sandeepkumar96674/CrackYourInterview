class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_map = {}
        i = 1
        b_rev = board[::-1]
        for d, r in enumerate(b_rev):
            if d%2 != 0: r = r[::-1] 
            for s in r:
                board_map[i] = s
                i += 1
        q = [(1, 0)]
        v = set()
        goal = len(board) * len(board) 
        while q:
            curr, moves = q.pop(0)
            if curr == goal: return moves
            for i in range(1, 7):
                if curr+i > goal: continue
                next_pos = curr+i if board_map[curr+i] == -1 else board_map[curr+i]
                if next_pos not in v:
                    v.add(next_pos)
                    q.append((next_pos, moves+1))
        return -1
 