class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # lets try recursion and backtracking
        ans = []
        
        def recurse(nums, idx, ans):
            #end case
            if idx == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                recurse(nums, idx+1, ans)
                nums[idx], nums[i] = nums[i], nums[idx]


     
        recurse(nums, 0, ans)
        return(ans)

        
        