from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_freq = 0 
        max_count = 0
        count = defaultdict(int)
        
        while r < len(s):
            count[s[r]] += 1
            #r += 1
            max_freq = max(max_freq, count[s[r]])

            while (r-l+1) - max_freq > k: #needs shrinking
                count[s[l]] -= 1
                l += 1


            max_count = max(max_count, (r-l+1))
            r += 1
        return max_count