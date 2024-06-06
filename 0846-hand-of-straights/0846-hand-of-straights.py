class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        nums.sort() 
        nums = Counter(nums) 
        while nums:
            num = list(nums.keys())[0]
            for i in range(k): 
                if nums[num + i] == 0:
                    return False
                nums[num+i] -= 1
                if nums[num+i] == 0:
                    nums.pop(num+i)
        return True