class Solution:
    def subLinkedList(self, l1, l2): 
        arr=[]
        while l1:
            arr.append(l1.data)
            l1=l1.next
        arr2=[]
        while l2:
            arr2.append(l2.data)
            l2=l2.next
        str1="".join(str(x) for x in arr)
        str2="".join(str(x) for x in arr2)
        k=int(str1)
        j=int(str2)
        if k>j:
            ans=k-j
        else:
            ans=j-k
        t=str(ans)
        new=LinkedList()
        for i in range(len(t)):
            new.insert(int(t[i]))
        return new.head