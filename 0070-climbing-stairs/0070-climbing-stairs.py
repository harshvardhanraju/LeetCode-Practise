class Solution:
    def climbStairs(self, n: int) -> int:
        dp =[0] * (n+1) #signifies number of steps it will take to reach ith index
        dp[0] = dp[1] =  1 #steps to reach 0 or 1st level is 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

