class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        u,y,x=set(),defaultdict(list),defaultdict(list)
        def f(p,q):[u.add((p,q)),(r:=y[p])and(y.__delitem__(p),{(p,t) in u or f(p,t)for t in r}),(c:=x[q])and(x.__delitem__(q),{(t,q) in u or f(t,q)for t in c})]
        for a,b in s:y[a]+=[b] ; x[b]+=[a]
        return sum((v:=len(u),f(*p),max(len(u)-v-1,0))[-1]for p in s)