class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref, n, summ = {0:-1}, len(nums), 0
        for i in range(n):
            summ += nums[i]
            sdivk = summ%k
            if sdivk in pref:
                if i-pref[sdivk] > 1:
                    return True
            else:
                pref[sdivk] = i
        return False
                