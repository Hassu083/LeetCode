class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s) 
        ans = []
        
        @lru_cache(None) 
        def check(i,j):
            if i<j:
                return s[i] == s[j] and check(i+1, j-1) 
            return True
        
        def solve(i, sub):
            if i == n:
                ans.append(sub) 
            for j in range(i, n):
                if check(i,j):
                    solve(j+1, sub+[s[i:j+1]]) 
        
        solve(0, []) 
        
        return ans