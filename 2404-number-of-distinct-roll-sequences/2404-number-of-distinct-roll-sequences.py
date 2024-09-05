class Solution:
    def distinctSequences(self, n: int) -> int:

        gcd_map = {
            1: [2,3,4,5,6],
            2: [1,3,5],
            3: [1,2,4,5],
            4: [1,3,5],
            5: [1,2,3,4,6],
            6: [1,5]
        }

        @lru_cache(None)
        def dp(i, second_last, last):
            if i == n: return 1
            aans = 0
            for k in gcd_map[last]:
                if k == second_last: continue
                aans += dp(i+1, last, k)
            return aans

        return sum(dp(1, -1, k) for k in range(1, 7))%1_000_000_007



        