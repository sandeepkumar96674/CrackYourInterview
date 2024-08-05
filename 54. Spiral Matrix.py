class Solution(object):
    def spiralOrder(self, matrix):
		#firstly we will initialize 4 pointers-left,right,top,bottom..
        left=top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        arr=[]
        
        while True:
            if left>right:
                break
            for i in range(left,right+1):
                arr.append(matrix[top][i])
            top+=1

            if bottom<top:
                break
            for i in range(top,bottom+1):
                arr.append(matrix[i][right])
            right-=1
            
            if left>right:
                break 
            for i in range(right,left-1,-1):
                arr.append(matrix[bottom][i])
            bottom-=1
            
            if bottom<top:
                break
            for i in range(bottom,top-1,-1):
                arr.append(matrix[i][left])
            left+=1
            
        return arr