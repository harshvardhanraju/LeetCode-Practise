class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # valid palindrome

        result = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd = expandAroundCenter(i, i)
            if len(odd) > len(result):
                result = odd
            
            # Even-length palindrome
            even = expandAroundCenter(i, i+1)
            if len(even) > len(result):
                result = even

        return result
