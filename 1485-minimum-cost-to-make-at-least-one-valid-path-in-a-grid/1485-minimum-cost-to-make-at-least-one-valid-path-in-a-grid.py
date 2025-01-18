class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def valid(x, y):
            return 0<=x<m and 0<=y<n

        costs = [[math.inf]*n for _ in range(m)]
        dir = [0, 1, 0, -1, 0]
        nums_dir = [1, 3, 2, 4]
        Q = [(0, 0, 0)]
        costs[0][0] = 0
        while Q:
            cost, i, j = heappop(Q)
            for k in range(4):
                x, y = i+dir[k], j+dir[k+1]
                num_dir = nums_dir[k]
                if valid(x, y):
                    new_cost = cost + int(grid[i][j] != num_dir)
                    if new_cost < costs[x][y]:
                        costs[x][y] = new_cost
                        heappush(Q,(new_cost, x, y))
        
        return costs[m-1][n-1]