#User function Template for python3

class TwoStacks:
    def __init__(self):
        self.num=100
        self.arr=[None]*self.num
        self.top1=-1
        self.top2=self.num
        
    # Function to push an integer into stack 1
    def push1(self, x):
        if self.top1 < self.top2 -1:
            self.top1+=1
            self.arr[self.top1]=x
        else:
            return -1

    # Function to push an integer into stack 2
    def push2(self, x):
        if self.top1 < self.top2 -1:
            self.top2-=1
            self.arr[self.top2]=x
        else:
            return -1

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.top1>=0:
            val=self.arr[self.top1]
            self.top1-=1
            return val
        else:
            return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.top2<self.num:
            val=self.arr[self.top2]
            self.top2+=1
            return val
        else:
            return -1