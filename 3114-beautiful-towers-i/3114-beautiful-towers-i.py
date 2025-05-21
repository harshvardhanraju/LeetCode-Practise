class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        l_sum = [0] * (n) 
        r_sum = [0] * (n) 
        stack = [] #stores index
        max_sum = 0
        #monotic increasing stack built from left
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                prev_idx = stack.pop()
            
            if stack :
                prev_idx = stack[-1]
                l_sum[i] = l_sum[prev_idx] + (i-prev_idx) * heights[i]
            else:
                 l_sum[i] = (i + 1) * heights[i]
            stack.append(i)
            
        stack = [] 
        #monotic increasing stack built from back
        for i in reversed(range(n)):
            while stack and heights[i] < heights[stack[-1]]:
                prev_idx = stack.pop()
            
            if stack :
                prev_idx = stack[-1]
                r_sum[i] = r_sum[prev_idx] + (prev_idx - i) * heights[i]  #D-P memoisation used
            else:
                 r_sum[i] = (n - i) * heights[i]
            stack.append(i)

        for i in range(n):
            #calculate lsum and rsum with 2 monotonic stacks
            # print("for val of i, lsum and rsum are: ", heights[i], l_sum[i], r_sum[i])
            max_sum = max(max_sum, l_sum[i] + r_sum[i] - heights[i])
        
        return max_sum
