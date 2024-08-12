with open('user.out', 'w') as f:
    outs = []
    for temp in map(loads, stdin):
        stack=[]
        result=[0]*len(temp)
        for index,value in enumerate(temp):
            while stack and value>temp[stack[-1]]:
                result[preIndex]=index-(preIndex:=stack.pop())
            stack.append(index)
        outs.append(f"[{','.join([str(x) for x in result])}]\n")
    f.writelines(''.join(outs))
exit()