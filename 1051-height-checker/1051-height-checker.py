class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = [0] * 101
        for height in heights:
            exp[height] += 1
        ans, j = 0, 0
        for i in range(1, 101):
            if exp[i]:
                for _ in range(exp[i]):
                    if i!=heights[j]:
                        ans += 1
                    j += 1
        return ans