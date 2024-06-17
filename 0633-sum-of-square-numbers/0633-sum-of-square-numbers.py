class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        num1 = 0 
        while num1*num1 <= c:
            num2 = c - num1*num1
            underRootNum2 = int((num2)**0.5)
            if underRootNum2**2 == num2:
                return True
            num1 += 1
        return False