class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            for i in range(len(ans)):
                copy = ans[i].copy() 
                copy.append(num) 
                ans.append(copy) 
        return ans