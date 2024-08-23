import re
class Solution:
    def displayContacts(self, n, contact, s):
        contact=list(set(contact)) 
        contact.sort() 
        m=len(s)
        ans=[[]]*m
        str=""
        for i in range(m):
            str+=s[i]
            for name in contact:
                res=re.match(str,name,re.IGNORECASE)
                if res:
                    if ans[i]:
                        ans[i].append(name)
                    else:
                        ans[i]=[name]
        for l in ans:
            if not l:
                l.append(0)
        return ans