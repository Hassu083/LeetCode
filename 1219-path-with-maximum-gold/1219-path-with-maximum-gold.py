class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        DIR = [0, 1, 0, -1, 0]
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0:
                return 0
            ans = 0
            temp = grid[i][j]
            grid[i][j] = 0
            for k in range(4):
                ans = max(ans, temp+dfs(i+DIR[k], j+DIR[k+1]) ) 
            grid[i][j] = temp
            return ans
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j)) 
        return ans