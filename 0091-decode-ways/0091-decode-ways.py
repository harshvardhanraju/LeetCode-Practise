class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] =='0':
            return 0 
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        if len(s) == 1:
            return 1

        if 10 <= int(s[0:2]) <= 26 and s[1] != '0':
            dp[1] = 2
        elif s[1] == '0':
            if s[0] == '1' or s[0] == '2':
                dp[1] = 1
            else:
                return 0  # Invalid decoding
        else:
            dp[1] = 1
        
        
        for i in range(2, n):
            #single digit combo
            if s[i] != '0':
                dp[i] = dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n-1]
        