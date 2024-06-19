class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n, total_flowers = len(bloomDay), m*k
        maxArray = [0]*n
        
        if total_flowers>n:
            return -1
        elif total_flowers == n:
            return max(bloomDay)
        
        l, r, ans = 0, max(bloomDay), math.inf
        while l <= r:
            mid = (l+r)>>1
            
            i, j, bouquets = 0, 0, 0
            while j < n:
                i = j
                while j < n and bloomDay[j] <= mid:
                    j += 1
                bouquets += (j-i)//k
                j += 1
            
            if bouquets >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
                
                        
    
        