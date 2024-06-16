class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach, ln, ans, idx = 0, len(nums), 0, 0
        while reach < n:
            while idx < ln and reach + nums[idx] <= 2*reach+1:
                reach += nums[idx]
                idx += 1
            if reach < n:
                reach = 2*reach + 1
                ans += 1
        return ans
        