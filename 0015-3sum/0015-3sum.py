class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values
                continue
            if len(nums) < 3:  # Edge case: fewer than 3 numbers
                return triplets  
            left = i+1
            right = len(nums)-1
            while left < right:
                if (nums[i] + nums[left] + nums[right]) > 0:
                    right -= 1
                elif (nums[i] + nums[left] + nums[right]) < 0:
                    left += 1
                else: #important section when 3sum found
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1 
                    right -= 1
        return triplets

                
                      

        