class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        last_number, ans = -1, 0
        for num in nums:
            if num >= last_number:
                last_number = num + 1
            else:
                ans += last_number-num
                last_number += 1
        return ans
                