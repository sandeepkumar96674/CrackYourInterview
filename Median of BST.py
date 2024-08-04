def findMedian(root):
    if not root:
        return -1
    temp = []
    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        temp.append(node.data)
        dfs(node.right)
    dfs(root)
    n = len(temp)
    if n%2 == 0:
        out = (temp[n//2]+temp[(n//2)-1])/2
        if int(out) == out:
            return int(out)
        else:
            return out
    return temp[n//2]