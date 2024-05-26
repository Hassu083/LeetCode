class Solution:
    def checkRecord(self, n: int) -> int:
        prev = [[1]*3 for _ in range(2)]
        for i in range(n, 0, -1):
            dp = [[0]*3 for _ in range(2)]
            for numberOfAbsents in range(2):
                for late in range(3):
                    dp[numberOfAbsents][late] += prev[numberOfAbsents][0]
                    if numberOfAbsents < 1:
                        dp[numberOfAbsents][late] += prev[numberOfAbsents+1][0]
                    if late < 2:
                        dp[numberOfAbsents][late] += prev[numberOfAbsents][late+1]
                    dp[numberOfAbsents][late] %= 1000000007
            prev = dp
        return dp[0][0] % 1_000_000_007
            