class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        stack = []
        operators = ['+', '-', '*', '/']
        for i in S:
            if i in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                if i == '+':
                    ans = (n2 + n1)
                elif i == '-':
                    ans = (n2 - n1)
                elif i == '*':
                    ans = (n2 * n1)
                else:
                    ans = (n2 // n1)
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack[0]