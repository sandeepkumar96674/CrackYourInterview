class Solution:
    def Anagrams(self, words, n):
        d={}
        for i in words:
            w="".join(sorted(i))
            if w not in d.keys():
               d[w]=[i]
            else:
                d[w].append(i)
        return d.values()