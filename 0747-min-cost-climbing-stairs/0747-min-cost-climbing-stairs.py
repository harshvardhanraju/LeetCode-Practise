class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp =[0] * (n+1) #signifies number of steps it will take to reach ith index
        dp[0] = cost[0] 
        dp[1] = cost[1] #steps to reach 0 or 1st level is 1
        for i in range(2, n):
            dp[i] = min(cost[i] + dp[i-2], cost[i] + dp[i-1])
            # print(dp)

        return min(dp[n-1], dp[n-2])
        