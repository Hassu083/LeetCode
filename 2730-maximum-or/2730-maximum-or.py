class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        
        bitwiseOr = lambda x, y: x | y
        
        forward = list(accumulate(nums, bitwiseOr))
        backward = list(accumulate(nums[ : : -1], bitwiseOr))[ : : -1]
        
        forward = [0] + forward[ : -1]
        backward = backward[1 : ] + [0]
        
        res = 0
        
        for i in range(len(nums)):
            total = forward[i] | backward[i]
            t = nums[i] * pow(2, k)
            
            res = max(res, total | t)
        
        return res