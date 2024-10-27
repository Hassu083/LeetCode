class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:


        MOD = 10**9 + 7
        n = len(nums)

        @lru_cache(None)
        def dp(i, g1, g2):
            if i >= n:
                if g1 and g2 and g1 == g2:
                    return 1
                return 0
            value = dp(i+1, g1, g2) + dp(i+1, gcd(g1, nums[i]), g2) + dp(i+1, g1, gcd(g2, nums[i]))
            # print((i, g1, g2), "-->", value)
            return value
        
        return dp(0, 0, 0)%MOD