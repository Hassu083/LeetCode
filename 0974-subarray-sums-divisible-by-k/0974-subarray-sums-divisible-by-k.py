class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hm, n, _sum, ans = {0: 1}, len(nums), 0, 0
        for i in range(n):
            _sum += nums[i]
            sdivk = _sum%k
            sans = hm.get(sdivk, 0) 
            hm[sdivk] = sans + 1
            ans += sans
        return ans