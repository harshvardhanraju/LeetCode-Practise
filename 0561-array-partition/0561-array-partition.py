class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total_sum = 0
        
        for val in nums[::2]:
            total_sum += val
        return total_sum

        