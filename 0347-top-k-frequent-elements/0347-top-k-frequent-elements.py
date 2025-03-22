class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using hashmap for frequency count
        # hashmap = {}
        # for num in nums:
        #     hashmap[num] = hashmap.get(num, 0) + 1
        dicti = Counter(nums)

        # using Max-heap for frequency sorting
        heap = []
        for item, freq in dicti.items():
            heapq.heappush(heap, (freq, item))
        
        top_k = heapq.nlargest(k, heap)  # ➝ [5, 3] (Get 2 largest)
        # Extract only the second elements
        result = [x[1] for x in top_k]
        return result