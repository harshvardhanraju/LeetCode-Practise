class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() 
        def backtrack(start, state, cur_sum):
            if cur_sum == target:
                result.append(list(state))
                return
            
            if cur_sum > target: # pruning trees for cases that are not required
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                state.append(candidates[i])
                backtrack(i + 1, state , cur_sum + candidates[i])
                state.pop()
            
        backtrack(0, [], 0)

        return result