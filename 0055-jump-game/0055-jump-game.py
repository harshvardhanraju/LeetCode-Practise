class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = len(nums) - 1
        farthest = 0
        if len(nums) == 1:
            return True
        for idx, val in enumerate(nums[:-1]):
            if farthest >= idx:
                farthest = max(farthest, idx + val)
                if farthest >= target:
                    return True
        return False
            


        
        