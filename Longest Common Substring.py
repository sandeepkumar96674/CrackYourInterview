class Solution:
    def longestCommonSubstr(self, str1, str2):
        max_len=0
        for i in range(len(str1)):
            for j in range(i,len(str1)):
                s=str1[i:j+1]
                if s in str2:
                    max_len=max(max_len,len(s))
        return max_len