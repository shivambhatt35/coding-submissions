class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    
        n = len(position)
        arr = [(p,v) for p,v in zip(position, speed)]

        sorted_arr = sorted(arr, reverse = True)
        stack = []

        for i in sorted_arr:

            pos = i[0]
            speed = i[1]

            stack.append((target-pos)/speed)

            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        