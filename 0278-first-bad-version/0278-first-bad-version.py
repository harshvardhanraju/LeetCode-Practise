# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        # mid = (left + right) // 2
        while left < right:
            mid = (left + right) // 2
            val = isBadVersion(mid)
            if val: #true
                right = mid 
            else:
                left = mid + 1
            
        return left 
        
    