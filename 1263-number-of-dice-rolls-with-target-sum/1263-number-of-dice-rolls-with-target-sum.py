class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        k += 1

        @lru_cache(None)
        def dp(i, s):
            if i == n:
                return s == target
            ans = 0
            for j in range(1, k):
                if s+j <= target:
                    ans += dp(i+1, s+j)
            return ans%1_000_000_007

        return dp(0, 0)
        