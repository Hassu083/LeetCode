class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        for bit in s:
            if bit == "1":
                num = num | 1
            num <<= 1
        num >>= 1
        steps = 0
        while num != 1:
            num = num + 1 if num%2 else num >> 1
            steps += 1
        return steps
            