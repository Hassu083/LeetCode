class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans, count, minimum_change = 0, 0, float("inf") 
        for num in nums:
            ans += num
            change = (num^k) - num
            if change > 0:
                ans += change
                count += 1
            minimum_change = min(minimum_change, abs(change))
        if count%2 == 1:
            ans -= minimum_change
        return ans