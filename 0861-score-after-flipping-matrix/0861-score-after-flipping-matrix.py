class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        count = [0]*n
        def tg(x):
            return 0 if x else 1
        ans = 0
        for row in grid:
            toggle = row[0] == 0
            subans = 0
            for j in range(n):
                subans <<= 1
                bit = tg(row[j]) if toggle else row[j]
                count[j] += bit
                subans |= bit
            ans += subans
        mask = 1
        for j in range(n-1, -1, -1):
            one, zero = count[j], m-count[j]
            if zero > one:
                ans += (zero-one)*mask
            mask <<= 1
        
        return ans