class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0
        for i in nums:
            if cursum < 0:
                cursum = 0
            cursum += i
            maxsum = max(maxsum, cursum)
        return maxsum