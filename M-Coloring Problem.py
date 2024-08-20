def graphColoring(graph, k, V):
    color = [0]*V
    def isPossible(node, col):
        for v in range(V):
            if v != node and graph[node][v] == 1 and color[v] == col:
                return False
        return True
    def fun(node):
        if node == V:
            return True
        for col in range(1, k + 1):
            if isPossible(node, col):
                color[node] = col
                if fun(node + 1):
                    return True
                color[node] = 0
        return False
    return fun(0)