class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        i, possible_profit, n = 0, [], len(projects)
        for _ in range(k):
            while i<n and projects[i][0] <= w:
                heappush(possible_profit, -projects[i][1])
                i += 1
            if possible_profit:
                w -= heappop(possible_profit)
        return w