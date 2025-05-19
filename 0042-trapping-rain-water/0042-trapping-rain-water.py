class Solution:
    def trap(self, height: List[int]) -> int:
        lidx = 0
        total_water = 0
        n = len(height)
        max_l, max_r = [0] * n, [0] * n
        max_l[0] = height[0]

        for i in range(1, n):
            max_l[i] = max(max_l[i-1], height[i])
        
        max_r[n - 1] = height[n - 1]
        for i in range(n -2 , -1, -1):
            max_r[i] = max(max_r[i+1], height[i])

        print(max_l)
        for i in range(n):
            water = min(max_l[i], max_r[i]) - height[i]
            print(water)
            total_water += water
        return total_water