class Solution:
    
    def rabin_karp(self,text, pattern):
        d, q, n, m = 256, 101, len(text), len(pattern)
        h, p, t = ((d**(m-1))% q), 0, 0
        res = []
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
    
        for i in range(n - m + 1):
            if p == t and text[i:i + m] == pattern:
                res.append(i+1)
            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                t = (t + q) % q  # Ensure non-negative
    
        return res
    def search(self, pattern, text):
        # code here
        return self.rabin_karp(text,pattern)
