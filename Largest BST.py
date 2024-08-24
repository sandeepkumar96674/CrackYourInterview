class Solution:
    def largestBst(self, root):
        def fun(ptr):
            if not ptr:
                return float('inf'),float('-inf'),0
            if not ptr.left and not ptr.right:
                return ptr.data,ptr.data,1
            left_min,left_max,countl=fun(ptr.left)
            right_min,right_max,countr=fun(ptr.right) 
            if left_max < ptr.data < right_min:
                current_min = min(left_min, ptr.data)
                current_max = max(right_max, ptr.data)
                bst_size = countl + countr + 1
                ans[0] = max(ans[0], bst_size)
                return current_min, current_max, bst_size
            return float('-inf'),float('inf'),0
        ans=[1]
        fun(root)
        return ans[0]