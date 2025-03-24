class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        lsum, rsum = [0]*n, [0]*n
        if n==1:
            return 0 #single element is the pivot ele
        for i in range(1, n):
            lsum[i] = lsum[i-1] + nums[i-1]
            rsum[n-i-1] = rsum[n-i] + nums[n-i]
        
        for i in range(n):
            if lsum[i] == rsum[i]:
                return i
        return -1

