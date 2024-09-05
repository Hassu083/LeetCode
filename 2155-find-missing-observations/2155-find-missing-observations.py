class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = mean*(n+m) - sum(rolls)
        
        if not (n <= s <= 6*n):
            return []
        
        ans = [s//n]*n
        for i in range(s%n):
            ans[i] += 1
        return ans
                
        