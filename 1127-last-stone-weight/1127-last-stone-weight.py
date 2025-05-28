import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stack = []
        for stone in stones:
            heapq.heappush(stack, -(stone))
        if len(stack) <= 1:
            return stones[0]
        # heapq.heapify(stones)
        while len(stack) >=2:
            val1 = heapq.heappop(stack)
            val2 = heapq.heappop(stack)

            if val1 == val2:
                continue
            else:
                heapq.heappush(stack, -(abs(abs(val2) - abs(val1))))
        
        if stack:
            return -(heapq.heappop(stack))
        else:
            return 0