class Solution:
    def mincostToHireWorkers(self, q: List[int], w: List[int], k: int) -> float:
        n = len(q)
        pairs = sorted([(w[i]/q[i], q[i]) for i in range(n)])
        
        heap, ans, quality = [], math.inf, 0
        for r, q in pairs:
            heappush(heap, -q)
            quality += q
            
            if len(heap) > k:
                quality += heappop(heap)
            if len(heap) == k:
                ans = min(ans, quality*r)
        
        return ans