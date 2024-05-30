class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        map,count,subtract, ans, xor = {0:0},{0:1},{0:0}, 0, 0
        
        for i in range(len(arr)):
            xor ^= arr[i]
            if xor in map:
                j = map[xor]
                ans += max(0, count[xor]*(i-j)-subtract[xor])
                subtract[xor] += i-j+1
            else:
                map[xor] = i+1
                subtract[xor] = 0
                count[xor] = 0
            count[xor] += 1 
        return ans
                