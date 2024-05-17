class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        ans = [0]*n
        graph = defaultdict(set) 
        for a, b in paths:
            graph[a-1].add(b-1) 
            graph[b-1].add(a-1)  
        for i in range(n):
            if ans[i] == 0:
                q = deque([i])
                vis = {i}
                while q:
                    node = q.popleft() 
                    color = {1, 2,3,4}
                    for child in graph[node]:
                        if ans[child] == 0:
                            if child in vis: continue
                            q.append(child)
                            vis.add(child)
                        elif ans[child] in color:
                            color.remove(ans[child]) 
                    ans[node] = color.pop() 
        return ans