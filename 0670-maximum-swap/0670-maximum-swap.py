class Solution:
    def maximumSwap(self, num: int) -> int:
        #hashmap to store num:leftmost idx
        last_pos = {}
        num = [int(d) for d in str(num)]
        n = len(num)
        r_max = [0] * n
        r_max[n-1] = num[n-1]
        for i in range(n-2, -1, -1):
            r_max[i] = max(r_max[i+1], num[i])
            
            
        last_pos = {int(d): i for i, d in enumerate(num)}  # stores rightmost positions        
        i = 0 
        
        while i < n:
            if num[i] < r_max[i]:
                swap = True
                temp = num[i]
                num[i] = r_max[i]
                num[last_pos[r_max[i]]] = temp
                result = int(''.join(str(d) for d in num))
                return result
            i += 1
        result = int(''.join(str(d) for d in num))

        return result
        
        