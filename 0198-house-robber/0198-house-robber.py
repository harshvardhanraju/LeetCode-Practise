class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a, b = b, max(nums[i] + a, b)
        return b
        