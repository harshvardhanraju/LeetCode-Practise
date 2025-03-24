class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # brute force - O(n2)
        answer = [0] * (n+1)
        # for i, val in enumerate(bookings):
        #     start = val[0]-1
        #     end = val[1]
        #     value = val[2]
        #     for j in range(start, end):
        #         answer[j] += value
        #     print(answer)
        # return answer
        for val in bookings:
            start = val[0]-1
            end = val[1]
            value = val[2]
            answer[start] += value
            answer[end] -= value
        for i in range(1, len(answer)):
            answer[i] += answer[i-1]

        return answer[:n]
            

        