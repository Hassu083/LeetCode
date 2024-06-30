class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        prev = [[0]*3 for _ in range(3)]
        for i in range(n):
            dp = [[0]*3 for _ in range(3)]
            nums[i] %= 2
            for num in range(3):
                for k in range(3):
                    dp[num][k] = max(dp[num][k], prev[num][k])
                    taken = 0
                    if  num == 2:
                        taken = 1+prev[num][k]
                    elif k == 2:
                        taken = 1+prev[num][(nums[i]+num)%2]
                    elif (nums[i]+num)%2 == k:
                        taken = 1+prev[num][k]
                    dp[nums[i]][k] = max(dp[nums[i]][k], taken)
            prev = dp
        return max(max(i) for i in dp)