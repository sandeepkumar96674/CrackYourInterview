
class Solution:
    def multiply_two_lists(self, first, second):
        mod = 10**9 + 7
        n1, n2 = 0, 0
        while first:
            n1 = (n1 * 10 + first.data) % mod
            first = first.next
        while second:
            n2 = (n2 * 10 + second.data) % mod
            second = second.next
        return (n1 * n2) % mod