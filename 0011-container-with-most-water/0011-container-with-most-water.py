class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        area = 0
        max_area = 0
        for i in range(len(height)):
            area = (r-l) * min(height[r], height[l])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        