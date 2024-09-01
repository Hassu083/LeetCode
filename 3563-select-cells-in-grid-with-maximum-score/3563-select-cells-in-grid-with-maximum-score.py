class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        values = defaultdict(list)
        for i in range(m):
            for val in grid[i]:
                values[val].append(i)
        values = list(values.items())
        n = len(values)
        self.ans = 0
        
        @lru_cache(None)
        def maxSum(i, mask):
            if i == n:
                return 0
            ans = maxSum(i+1,mask)
            for row in values[i][1]:
                if not mask&(1<<row):
                    ans = max(ans, values[i][0] + maxSum(i+1,mask|(1<<row)))
            return ans
        
        return maxSum(0,0)
        