class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = defaultdict(int)

        prefix_sum[0] = 1

        curr_sum = 0
        count = 0

        for i in nums:

            curr_sum+=i

            target = curr_sum - k

            if target in prefix_sum:
                count+=prefix_sum[target]
            
            prefix_sum[curr_sum]+=1
        
        return count
        