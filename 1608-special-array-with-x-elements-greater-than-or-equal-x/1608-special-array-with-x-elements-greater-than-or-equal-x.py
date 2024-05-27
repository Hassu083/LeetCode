class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort() 
        n = len(nums)
        for i in range(n):
            if n-i <= nums[i] and (i==0 or n-i > nums[i-1]) :
                return n-i 
        return -1