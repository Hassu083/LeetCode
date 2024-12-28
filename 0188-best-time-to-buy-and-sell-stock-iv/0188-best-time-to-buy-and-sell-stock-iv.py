class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)
        memo = [[[-1]*(2) for i in range(k+1)] for _ in range(n+1)]
        
        def dp(i, k, isBuy):
            if k == 0 or i >= n:
                return 0
            if memo[i][k][int(isBuy)] != -1:
                return memo[i][k][int(isBuy)]
            
            if isBuy:
                memo[i][k][int(isBuy)] = max(-prices[i]+dp(i+1, k, not isBuy), dp(i+1, k, isBuy))
                return memo[i][k][int(isBuy)]
            memo[i][k][int(isBuy)] = max(prices[i]+dp(i+1, k-1, not isBuy), dp(i+1, k, isBuy))
            return memo[i][k][int(isBuy)]
        
        print(dp(0, k, True))

        

        return max(max(row) for row in memo[0])

        