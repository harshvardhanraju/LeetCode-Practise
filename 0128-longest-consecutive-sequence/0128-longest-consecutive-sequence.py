class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        if len(hset) <= 1:
            return len(hset)
        max_len = 0
        for num in hset:
            lenght = 1
            if num-1 not in hset:
                while num+lenght in hset:
                    lenght += 1
                max_len = max(lenght, max_len)
        return max_len



        