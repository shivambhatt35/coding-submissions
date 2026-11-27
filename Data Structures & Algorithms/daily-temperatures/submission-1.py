class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)

        res = [0]*n
        stack = []

        for i, v in enumerate(temperatures):

            while stack and v > stack[-1][1]:

                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
        
            stack.append((i,v))
        
        return res
        