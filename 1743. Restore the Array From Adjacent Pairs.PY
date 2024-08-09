class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        ans = [float('inf')] * (len(adjacentPairs) + 1)
        for [n1, n2] in adjacentPairs:
            dic[n1].append(n2)
            dic[n2].append(n1)
        x = [key for key, value in dic.items() if len(value) == 1]
        ans[0], ans[len(adjacentPairs)] = x[0], x[1]
        ans[1] = dic[ans[0]][0]
        i = 1
        while i < len(adjacentPairs):
            y = ans[i]
            ans[i + 1] = dic[y][0] if dic[y][0] != ans[i - 1] else dic[y][1]
            i += 1
        return ans