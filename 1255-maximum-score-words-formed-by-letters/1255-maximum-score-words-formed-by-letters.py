class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = Counter(letters) 
        n = len(words) 
        memo = {}
        
        def dp(i,freq, memory):
            if i >= n:
                return 0
            key = (i, memory)
            if key in memo:
                return memo[key]
            
            ans = dp(i+1, freq, memory) 
            local_freq = Counter(words[i]) 
            
            if all(local_freq[ch] <= freq[ch] for ch in local_freq):
                freq_c = freq.copy() 
                sc = 0
                for ch in local_freq:
                    freq_c[ch] -= local_freq[ch]
                    sc += score[ord(ch)-ord("a")]*local_freq[ch]
                ans = max(ans, sc + dp(i+1, freq_c, str(freq_c.items())))
            memo[key] = ans
            return ans
        
        return dp(0, freq, str(freq.items())) 