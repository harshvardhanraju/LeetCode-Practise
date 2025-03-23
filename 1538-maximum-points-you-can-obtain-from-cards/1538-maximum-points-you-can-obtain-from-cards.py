class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum = 0
        if k >= len(cardPoints):
            return sum(cardPoints) 
        for i in range(k):
            lsum += cardPoints[i] 
        max_sum = lsum

        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i] 
            rsum += cardPoints[i-k]

            max_sum = max(max_sum, lsum+rsum)
        return max_sum


        