import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:

            if i in ('+','-','*','/'):

                a = int(stack[-1])
                stack.pop()
                b = int(stack[-1])
                stack.pop()

                if i == '+':
                    res = a+b
                elif i == '*':
                    res = a*b
                elif i == '/':
                    res = int(b/a)
                else:
                    res = b-a
                
                stack.append(int(res))
            
            else:
                stack.append(int(i))
        
        return stack[-1]