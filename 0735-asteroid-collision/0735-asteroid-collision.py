class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            collision = False
            while stack and  (val < 0 < stack[-1]): #collision condition
                if abs(val) < stack[-1]:
                    collision = True
                    break #as new asteriod is broken, no need to add to stack
                elif abs(val) > stack[-1]:
                    stack.pop() #last value gets broken, continue checking
                    # stack.append(val) #bigger asteroid gets added
                elif abs(val) == stack[-1]:
                    stack.pop() #last value gets broken and no new addition
                    collision = True
                    break
            if not collision:
                stack.append(val) #add value if no collision
            # print(stack)

        return stack