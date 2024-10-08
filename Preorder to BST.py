class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None
def Bst(pre, size):
    root = Node(pre[0])
    s = []
    s.append(root)
    i = 1
    while (i < size):
        temp = None
        while (len(s) > 0 and pre[i] > s[-1].data):
            temp = s.pop()
        if (temp != None):
            temp.right = Node(pre[i])
            s.append(temp.right)
        else:
            temp = s[-1]
            temp.left = Node(pre[i])
            s.append(temp.left)
        i = i + 1
    return root