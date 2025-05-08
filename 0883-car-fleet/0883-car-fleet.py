class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)
        time_to_target = [(target - pos)/speed for pos, speed in pairs]
        stack = []
        stack.append(time_to_target[0])
        for time in time_to_target[1:]:
            if time > stack[-1]:
                stack.append(time) #basically add only new car fleet/groups #becomes monotic decresasing stack
        return len(stack)

        