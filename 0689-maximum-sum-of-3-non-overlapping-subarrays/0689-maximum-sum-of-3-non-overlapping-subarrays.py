class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        pref = []
        s = 0
        for i,num in enumerate(nums):
            s += num
            if i >= k - 1:
                pref.append(s)
                s -= nums[i-k+1]
        
        n = len(pref)

        lm = [[0, 0] for _ in range(n)]
        lm[0] = [pref[0],0]
        for i in range(1, n):
            lm[i][0] = max(lm[i-1][0], pref[i])
            lm[i][1] = lm[i-1][1] if lm[i][0] == lm[i-1][0] else i

        rm = [[0, 0] for _ in range(n)]
        rm[-1] = [pref[-1], n-1]
        for i in range(n-2, -1, -1):
            rm[i][0] = max(rm[i+1][0], pref[i])
            rm[i][1] = i if pref[i] >= rm[i+1][0] else rm[i+1][1]
        
        s = 0
        ans = None
        for i in range(k, n-k):
            if (ns:=lm[i-k][0]+pref[i]+rm[i+k][0]) > s:
                s = ns
                ans = [lm[i-k][1], i, rm[i+k][1]]

        return ans