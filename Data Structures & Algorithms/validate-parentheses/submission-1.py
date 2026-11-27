class Solution:
    def isValid(self, s: str) -> bool:

        stack_arr = []

        dic = {']':'[', '}':'{', ')':'('}

        for i in s:

            if i in ('[','(','{'):
                stack_arr.append(i)
            else:
                if len(stack_arr)>0:
                    if stack_arr[-1] == dic[i]:
                        stack_arr.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack_arr)>0:
            return False
        
        return True
        