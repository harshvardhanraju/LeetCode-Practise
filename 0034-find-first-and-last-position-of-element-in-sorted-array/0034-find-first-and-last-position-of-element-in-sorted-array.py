class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        isStart = True

        def bs(nums, target, isStart):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    print(ans)
                    if isStart: # searching for starting index or first occurence, so minimum index req
                        right = mid - 1
                    else: # max index required
                        left = mid + 1
                    
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return ans


        
        return [bs(nums, target, True), bs(nums, target, False)] # return this only if found
        