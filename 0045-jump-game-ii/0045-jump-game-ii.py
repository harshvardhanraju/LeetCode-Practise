class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # DP approach
        min_jumps = [float('inf')] * n
        min_jumps[0] = 0 #starting pos is 0th index

        for i, val in enumerate(nums):
            for j in range(i + 1, min(i + val + 1, n)):
                cur_jump =  min_jumps[i] + 1
                min_jumps[j] = min(cur_jump, min_jumps[j])
        
        print(min_jumps)
        return min_jumps[-1]
        