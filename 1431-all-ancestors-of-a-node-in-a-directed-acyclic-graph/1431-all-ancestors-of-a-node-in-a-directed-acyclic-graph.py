class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ans = [[] for _ in range(n)]
        
        def merge(lst1, lst2, value):
            i, j = 0, 0
            m, n = len(lst1), len(lst2)
            ans = []
            valappend = False
            while i < m and j < n:
                if not valappend and value < lst1[i] and value < lst2[j]:
                    ans.append(value)
                    valappend = True
                elif lst1[i] < lst2[j]:
                    ans.append(lst1[i])
                    i += 1
                elif lst1[i] > lst2[j]:
                    ans.append(lst2[j])
                    j += 1
                else:
                    ans.append(lst1[i])
                    i += 1
                    j += 1
            if i < m:
                while i < m:
                    if not valappend and value < lst1[i]:
                        ans.append(value)
                        valappend = True
                    ans.append(lst1[i])
                    i += 1
            elif j < n:
                while j < n:
                    if not valappend and value < lst2[j]:
                        ans.append(value)
                        valappend = True
                    ans.append(lst2[j])
                    j += 1
            if not valappend:
                ans.append(value)
            return ans
        
        graph = defaultdict(list)
        inn = [0]*n
        for a, b in edges:
            graph[a].append(b)
            inn[b] += 1
        
        q = deque([i for i in range(n) if inn[i] == 0])
        while q:
            node = q.popleft()
            for child in graph[node]:
                ans[child] = merge(ans[child], ans[node], node)
                inn[child] -= 1
                if inn[child] == 0:
                    q.append(child)
        return ans
        