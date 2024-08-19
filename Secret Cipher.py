class Solution:
    def helper(self,s):
        lps = [0] * len(s)
        n = len(s)
        l,i = 0,1
        while (i < n):
            if s[i] == s[l]:
                l+=1
                lps[i] = l
                i+=1
            else:
                if (l==0):
                    lps[l] = 0
                    i+=1
                else:
                    l = lps[l-1]
        return lps 
    def compress(self, s):
        a = self.helper(s)
        n = len(s)
        ans = ""
        i = n - 1
        while (i > 0):
            if(i % 2 == 0):
                ans += s[i]
                i -= 1
                continue
            flag = False
            suffix = a[i]
            substr = i + 1
            if (suffix*2 >=substr):
                if (substr%(substr-suffix)) == 0:
                    if (substr /(substr - suffix)) % 2 ==0:
                        flag = True
            if flag:
                ans += "*"
                i = (i//2) + 1
            else:
                ans += s[i]
            i -= 1
            
        return s[0] + ans[::-1]