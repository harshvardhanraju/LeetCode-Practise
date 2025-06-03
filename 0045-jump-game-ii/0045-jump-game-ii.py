class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        cur_end = 0
        if len(nums) == 1:
            return 0
        
        for idx, val in enumerate(nums[:-1]):
            farthest = max(farthest, idx + val)
            if idx == cur_end:
                jumps += 1
                cur_end = farthest

        return jumps
            


        
        