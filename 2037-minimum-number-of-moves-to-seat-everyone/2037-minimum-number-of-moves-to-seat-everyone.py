class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        ans, n = 0, len(seats)
        for i in range(n):
            ans += abs(seats[i] - students[i])
        return ans