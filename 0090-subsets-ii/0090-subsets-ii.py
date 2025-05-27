class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []
        nums.sort()

        def recurse_set(nums, i, subset, res):
            if i == len(nums):
                res.append(list(subset))
                return
            #pick ith element
            subset.append(nums[i])
            #recurse
            recurse_set(nums, i + 1, subset, res)
            #not pick ith element
            subset.pop()
            #recurse
                        # skip duplicates when not picking
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            recurse_set(nums, i + 1, subset, res)
        
        recurse_set(nums, 0, subset, res)
        return(res)