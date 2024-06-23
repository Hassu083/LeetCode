class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minheap, maxheap, n, j, ans = [], [], len(nums), 0, 0
        
        def exclude(i, heap):
            while heap and heap[0][1] < i:
                heappop(heap) 

        for i in range(n):
            heappush(minheap, (nums[i], i))
            heappush(maxheap, (-nums[i], i))
            while minheap and maxheap and (-maxheap[0][0] - minheap[0][0]) > limit:
                j += 1
                exclude(j, minheap)
                exclude(j, maxheap)
            if minheap and maxheap:
                ans = max(ans, i - j + 1)
        
        return ans