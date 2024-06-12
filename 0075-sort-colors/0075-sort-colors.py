class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        zero, two, i = 0, n-1, 0
        while i<=two:
            if nums[i]==0:
                nums[i], nums[zero] = nums[zero], nums[i]
                while len(nums)>zero and nums[zero] == 0:
                    zero += 1
                i = zero
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            else:
                i += 1