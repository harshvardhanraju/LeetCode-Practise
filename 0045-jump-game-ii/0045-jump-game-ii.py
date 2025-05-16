class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # DP approach
        min_jumps = [float('inf')] * n
        min_jumps[0] = 0 #starting pos is 0th index

        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                min_jumps[j] = min(min_jumps[j], min_jumps[i] + 1)
                
        print(min_jumps)
        return min_jumps[-1]
        