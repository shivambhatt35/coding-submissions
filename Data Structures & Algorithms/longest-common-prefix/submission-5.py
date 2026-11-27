class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs = sorted(strs)
        n = len(strs)

        first = strs[0]
        last = strs[n-1]
        cnt = ""

        for i in range(0, len(first)):

            if first[i] == last[i]:
                cnt+=first[i]
            else:
                return cnt
        
        return cnt
        