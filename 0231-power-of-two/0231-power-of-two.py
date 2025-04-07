class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pow = 0
        def checkPow(n, pow):
            if(2**pow == n):
                return True
            elif(2**pow > n):
                return False
            return checkPow(n, pow +1)
        return checkPow(n, pow)
        