import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # stack = []
        # for num in nums:
        #     heapq.heappush(stack, -(num))
        
        # return -(heapq.nsmallest(k, stack)[-1])

        # Step 1: Build a min-heap with first k elements
        heap = nums[:k]
        heapq.heapify(heap)  # O(k)

        # Step 2: Process remaining elements
        for num in nums[k:]:
            if num > heap[0]:  # Only push if current num is larger than smallest in heap
                heapq.heappushpop(heap, num)  # Push new num and pop smallest

        return heap[0]  # kth largest is the smallest in the heap
        