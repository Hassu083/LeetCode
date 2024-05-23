class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        nums.sort() 
        
        def dp(i, j, kc):
            if i == n:
                return 1 if kc else 0
            ans = dp(i+1, j, kc) 
            if nums[i]-k not in j:
                ans += dp(i+1, j.union({nums[i]}), True) 
            return ans
        
        return dp(0, set(), False) 