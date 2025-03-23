class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lp, rp = 0, 0
        max_len = 0
        num_zero = 0
        for rp in range(len(nums)):
            if nums[rp] == 0:
                num_zero += 1
            while num_zero > k:
                if nums[lp] == 0:
                    num_zero -= 1
                lp += 1

            max_len = max(max_len, rp-lp+1)
        return max_len

