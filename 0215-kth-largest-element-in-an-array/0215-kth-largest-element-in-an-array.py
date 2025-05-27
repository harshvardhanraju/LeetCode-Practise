import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = []
        for num in nums:
            heapq.heappush(stack, -(num))
        
        return -(heapq.nsmallest(k, stack)[-1])
        