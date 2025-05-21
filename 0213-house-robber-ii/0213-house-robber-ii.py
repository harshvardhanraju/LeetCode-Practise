class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # make it 2 sub problems 
        #rob from 0 to n-1
        a = nums[0]
        b = max(nums[0], nums[1])
        
        for i in range(2, len(nums)-1):
            if i != len(nums):
                a, b = b, max(nums[i] + a, b)
        max1 = b
        #rob from 1 to n
        a = nums[1]
        b = max(nums[1], nums[2])
        
        for i in range(3, len(nums)):
            if i != len(nums):
                a, b = b, max(nums[i] + a, b)
        return max(max1, b)
        
        
            

        