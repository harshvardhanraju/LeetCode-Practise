class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        num_coins = len(piles) // 3
        piles.sort(reverse=True)
        #sorted_piles = sort(piles, reverse=True)
        sum1 = 0
        index = 1
        for _ in range(num_coins):
            sum1 += piles[index]
            index += 2
        return sum1


        return sum
            