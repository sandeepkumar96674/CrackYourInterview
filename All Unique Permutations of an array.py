class Solution:
    def uniquePerms(self, arr, n):
        result = []
        visited = [False]*n
        def backtrack(current_perm):
            if len(current_perm) == n:
                result.append(list(current_perm))
                return
            for i in range(n):
                if visited[i]:
                    continue
                if i > 0 and arr[i] == arr[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                current_perm.append(arr[i])
                backtrack(current_perm)
                current_perm.pop()
                visited[i] = False
        arr.sort()
        backtrack([])
        return sorted(result)
