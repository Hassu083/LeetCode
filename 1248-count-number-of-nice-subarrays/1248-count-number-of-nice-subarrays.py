class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def oddWithAtleastK(k):
            ans = 0
            count = 0
            j = 0
            for i in range(n):
                count += nums[i]%2
                while j < n and count > k:
                    count -= nums[j]%2
                    j += 1
                ans += i-j+1
            return ans
        return oddWithAtleastK(k) - oddWithAtleastK(k-1)