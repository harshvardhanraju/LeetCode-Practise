class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_satisfaction = sum(c for c, g in zip(customers, grumpy) if g == 0)

        extra_satisfaction = 0
        max_extra = 0

        # Compute extra satisfaction in the first window
        for i in range(minutes):
            if grumpy[i] == 1:
                extra_satisfaction += customers[i]
        max_extra = extra_satisfaction

        # Slide the window
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                extra_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                extra_satisfaction -= customers[i - minutes]
            max_extra = max(max_extra, extra_satisfaction)

        return base_satisfaction + max_extra