class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        
        left_prod = 1
        for i in range(n):
            result[i] = left_prod
            left_prod *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result