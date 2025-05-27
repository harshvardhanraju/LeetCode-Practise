class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(state, used):
            if len(state) == len(nums):
                result.append(list(state))
                return

            for i in range(len(nums)):
                if used[i] == True:
                    continue # skip this number as its used already
                else:
                    used[i] = True
                state.append(nums[i])
                backtrack(state, used)
                state.pop()
                used[i] = False
       
        backtrack([], [False] * len(nums))

        return result
        