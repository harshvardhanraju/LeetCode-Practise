class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = [0] * 1001
        for i, val in enumerate(trips):
            value = val[0]
            start = val[1]
            end = val[2]
            car[start] += value
            car[end] -= value # since passenger gets down at end position
        #runnign sum
        ssum = 0
        heap = []
        for i, val in enumerate(car):
            ssum += val
            heapq.heappush(heap, ssum)
        max_val = heapq.nlargest(1, heap)
        if max_val[0] > capacity:
            return False
        else:
            return True






        