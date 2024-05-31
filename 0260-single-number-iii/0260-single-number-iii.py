class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        memo = set() 
        for num in nums:
            if num in memo:
                memo.remove(num) 
            else:
                memo.add(num) 
        return list(memo) 