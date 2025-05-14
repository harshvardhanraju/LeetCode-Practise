class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #define the search space as its a search problem for min k
        max_piles = max(piles)
        left, right = 1, max_piles

        while left <= right:
            k = (left + right) // 2
            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile/k)
            
            if total_hours == h:
                right = k - 1 #search on the left for smaller values if they work
            elif total_hours > h:
                left = k + 1
            else:
                right = k - 1
        return left
             
        