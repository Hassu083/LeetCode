class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        
        n = len(nums) 
        ans = n*(n-1) >> 1
        visited = {}
        
        for i in range(n):
            diff = nums[i] - i
            if diff in visited:
                ans -= visited[diff]
                visited[diff] += 1
            else:
                visited[diff] = 1
        
        return ans
            
        