class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1: return 9//k
        
        def mul(lst):
            ans = 1
            for i in lst:
                ans *= i
            return ans
        
        @lru_cache(None)
        def factorial(n):
            if n == 0: return 1
            return n*factorial(n-1)
        
        N = factorial(n)
        N_1 = factorial(n-1)
        
        def numToPossiblities(nums:str):
            num = Counter(nums)
            ans = N//mul([math.factorial(count) for count in num.values()])
            if num["0"] != 0:
                num["0"] -= 1
                ans -= N_1//(mul(math.factorial(count) for count in num.values()))
            return ans
        

        
        ans = 0
        vis = set()
        for num in range(1, 10**(n//2)):
            char = str(num).zfill(n//2)
            if not char.endswith('0'):
                if n&1: char = [char[::-1] + str(mid) + char for mid in range(10)]
                else: char = [char[::-1] + char]
                for num in char:
                    int_num = int(num)
                    if int_num%k == 0:
                        char2 = tuple(sorted(num))
                        if char2 in vis:
                            continue

                        vis.add(char2)
                        ans += numToPossiblities(num)
        
        return ans