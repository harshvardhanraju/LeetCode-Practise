class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []
        result = [0] * len(nums)
        # square and add in heapq - O(n)
        for num in nums:
            heapq.heappush(heap, num * num)
        for i in range(len(nums)):
            result[i] = heapq.heappop(heap)
        return result
        