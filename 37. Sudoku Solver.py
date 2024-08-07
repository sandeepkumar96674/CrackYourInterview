class Solution:
    def solveSudoku(self, b: List[List[str]]) -> None:
        def s(i,j):
        
            if i==9:
                return True
        
            if b[i][j]==".":
                check = False
                
                for k in range(1,10):
                    k=str(k)
                    
                    if (k in rd[i] or k in cd[j] or k in bd[((i//3)*3)+(j//3)]):
                        h=0 #DO NOTHING  ;}
                    else:
                        rd[i].add(k)
                        cd[j].add(k)
                        bd[((i//3)*3)+(j//3)].add(k)
                        
                        b[i][j]=k
                        
                        if (j+1)==9:
                            check = s(i+1,0)
                        else:
                            check = s(i,j+1)
                        
                        if check:
                            break
                        
                        b[i][j]="."
                        
                        rd[i].remove(k)
                        cd[j].remove(k)
                        bd[((i//3)*3)+(j//3)].remove(k)
                
                if check:
                    return True
                return False
        
            else:
                if (j+1)==9:
                    return s(i+1,0)
                else:
                    return s(i,j+1)
        
        
        rd={0:set(),1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set()}
        cd={0:set(),1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set()}
        bd={0:set(),1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set()}
        
        for i in range(9):
            for j in range(9):
                rd[i].add(b[i][j])
                cd[j].add(b[i][j])
                bd[((i//3)*3)+(j//3)].add(b[i][j])
        
        s(0,0)
        
        return b