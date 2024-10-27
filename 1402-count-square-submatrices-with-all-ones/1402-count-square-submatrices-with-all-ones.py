class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    # print(i,j,matrix[i-1][j] if i-1>-1 else 0, matrix[i][j-1] if j-1>-1 else 0, matrix[i-1][j-1] if i-1>-1 and j-1>-1 else 0)
                    matrix[i][j] += min(matrix[i-1][j] if i-1>-1 else 0, matrix[i][j-1] if j-1>-1 else 0,  matrix[i-1][j-1] if i-1>-1 and j-1>-1 else 0)
                ans += matrix[i][j]
                print(ans)
        print(matrix)
        return ans


        