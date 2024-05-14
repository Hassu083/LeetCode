class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        @lru_cache(None)
        def dp0(i):
            if i>=n-1:
                return 0
            return max(nums[i]+dp0(i+2),dp0(i+1))
        
        @lru_cache(None)
        def dp(i):
            if i>=n:
                return 0
            return max(nums[i]+dp(i+2),dp(i+1))
        
        return max(dp0(0), dp(1))