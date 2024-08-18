class Solution:
    def countArrangement(self, n: int) -> int:
        def backstrap(pos :int, visited:int) -> int:
            if pos > n:
                return 1
            count = 0
            for i in range(1, n+1):
                if not visited & (1 << i) and (pos % i == 0 or i % pos == 0):
                    count += backstrap(pos + 1, visited | (1<<i))
            return count
        return backstrap(1,0)  