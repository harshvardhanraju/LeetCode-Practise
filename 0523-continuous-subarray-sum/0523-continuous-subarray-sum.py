class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        csum = 0
        visited = defaultdict(int)
        visited[0] = -1 # remainder of 0 is at -1?
        remainder = 0
        if len(nums) <= 1:
            return False
        for r in range(len(nums)):
            csum += nums[r]
            # remainder
            if k != 0:
                remainder = csum % k  
            else:
                remainder = csum  # Avoid division by zero error            
            
            # if remainder == 0:
            #     return True
            
            if remainder in visited:
                if (r - visited[remainder] >= 2): # and csum >= k:
                    return True
            if remainder not in visited:
                visited[remainder] = r
            # print(visited)
        return False
