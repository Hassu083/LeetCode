class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        ans, left_h, right_h, k_cond, n = [], [], [], k%2==0, len(nums) 
        
        def pushPop(h1, h2, ele):
            num, idx = heappushpop(h2, ele) 
            heappush(h1, (-num, idx)) 
                        
        def findMedian():
            if k_cond:
                return (right_h[0][0]-left_h[0][0])/2
            return left_h[0][0]*-1.0
        
        def delete(h, num):
            while h and h[0][1] <= num:
                heappop(h) 
        
        for i in range(k):
            if len(left_h) == len(right_h):
                pushPop(left_h, right_h, (nums[i], i)) 
            else:
                pushPop(right_h, left_h, (-nums[i], i))
                
        for i in range(k, n):
            ans.append(findMedian()) 
            if right_h and nums[i] >= right_h[0][0]: 
                heappush(right_h, (nums[i], i)) 
                if nums[i-k] <= -left_h[0][0]:
                    n, idx = heappop(right_h)
                    heappush(left_h, (-n, idx)) 
            else:
                heappush(left_h, (-nums[i], i)) 
                if nums[i-k] >= -left_h[0][0]:
                    n, idx = heappop(left_h) 
                    heappush(right_h, (-n, idx)) 
            delete(left_h, i-k)
            delete(right_h, i-k)
        
        ans.append(findMedian()) 
        
        return ans
            
        