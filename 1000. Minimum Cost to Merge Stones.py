class Solution:
    def mergeStones(self, piles: List[int], k: int) -> int:
        P = len(piles)
        if (P-1)%(k-1):
            return -1
        c = 0
        cs = [] 
        for p in piles:
            c += p
            cs.append(c)
        IMPOSSIBLE = float('inf')
        def acc(i: int, j: int) -> int:
            return cs[j] - (cs[i-1] if i else 0)
        @cache
        def cost(l: int, r: int, p: int) -> int:
            if l == r:
                return 0 if p == 1 else IMPOSSIBLE
            if p == 1:
                return cost(l, r, k) + acc(l, r)
            best = IMPOSSIBLE
            for L in range(1, r-l-p+3, k-1):
                best = min(best, cost(l, l+L-1, 1) + cost(l+L, r, p-1))
            return best
        return cost(0, P-1, 1)