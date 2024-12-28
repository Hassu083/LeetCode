class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        st = []
        for i, num in enumerate(prices):
            while st and prices[st[-1]] > num:
                st.pop()
            if st:
                ans = max(ans, num - prices[st[0]])
            st.append(i)
        
        @lru_cache(None)
        def dp(i, count, isBuy):
            if count == 0:
                return 0
            if i >= len(prices):
                return -math.inf
            if isBuy:
                return max(-prices[i]+dp(i+1, count, not isBuy), dp(i+1, count, isBuy))
            return max(prices[i]+dp(i+1, count-1, not isBuy), dp(i+1, count, isBuy))

        return max(ans, dp(0, 2, True))
        