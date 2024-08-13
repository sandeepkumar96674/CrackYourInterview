class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] 
        currentNode = root
        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            currentNode = stack.pop()
            k -= 1
            if k == 0:
                return currentNode.val
            currentNode = currentNode.right
        return None