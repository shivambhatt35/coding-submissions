from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Prepend each string with its character length followed by '#'
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Locate the '#' character to find where the length integer ends
            j = i
            while s[j] != '#':
                j += 1
            
            # Read the length prefix integer
            length = int(s[i:j])
            
            # Extract the exact string content of length 'length'
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # Advance pointer past the extracted string segment
            i = end

        return res
