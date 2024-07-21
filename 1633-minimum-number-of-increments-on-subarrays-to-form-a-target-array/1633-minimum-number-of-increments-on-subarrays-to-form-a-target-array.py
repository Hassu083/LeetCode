class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = 0
        prevdiff = 0
        for i in range(n):
            diff = target[i]
            if prevdiff != 0:
                if diff > prevdiff:
                    ans += diff - prevdiff
            else:
                ans += abs(diff)
            prevdiff = diff
    
        return ans    