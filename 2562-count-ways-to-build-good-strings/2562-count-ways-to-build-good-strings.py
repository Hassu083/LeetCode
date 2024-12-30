class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        memo = [1] + [0]*high
        M = 10**9+7
        ans = 0
        for i in range(high+1):
            if i-zero >= 0:
                memo[i] += memo[i-zero]
            if i-one >= 0:
                memo[i] += memo[i-one]
            memo[i] %= M
            if i >= low:
                ans = (ans + memo[i])%M

        return ans

        