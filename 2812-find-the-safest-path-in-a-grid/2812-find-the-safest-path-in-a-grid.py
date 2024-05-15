class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = deque() 
        vis = set() 
        dir = [0,1,0,-1,0]
        n = len(grid) 
        if grid[0][0] or grid[n-1][n-1]:
            return 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i,j))
                    vis.add((i,j)) 
        level = 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft() 
                grid[i][j] = level
                for k in range(4):
                    x, y = i+dir[k], j+dir[k+1]
                    if 0<=x<n and 0<=y<n and  (x, y) not in vis:
                        q.append((x, y)) 
                        vis.add((x, y)) 
            level += 1
        
        q = [(-grid[0][0], 0,0) ]
        vis = {(0,0)}
        while q:
            dis, i,j = heappop(q) 
            if i == j == n-1:
                return  dis*-1
            elif dis == 0:
                continue
            for k in range(4):
                x, y = i+dir[k], j+dir[k+1]
                if 0<=x<n and 0<=y<n and (x, y) not in vis:
                    heappush(q, (max(dis,-grid[x][y]),x, y)) 
                    vis.add((x, y)) 
        return 0