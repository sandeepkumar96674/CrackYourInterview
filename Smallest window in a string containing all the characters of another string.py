from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        p_count = Counter(p)
        s_count = Counter()
        start = 0
        min_len = float('inf')
        min_start = 0
        matched = 0
        
        for end in range(len(s)):
            s_count[s[end]] += 1
            
            if s[end] in p_count and s_count[s[end]] <= p_count[s[end]]:
                matched += 1
            while matched == len(p):
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_start = start
                
                s_count[s[start]] -= 1
                if s[start] in p_count and s_count[s[start]] < p_count[s[start]]:
                    matched -= 1
                start += 1
        if min_len == float('inf'):
            return "-1"
        else:
            return s[min_start:min_start + min_len]