class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        ans = math.inf
        left, right = 1, max(ranks)*cars*cars
        while left<=right:
            mid = (left+right)>>1
            noOfCars = sum(floor(sqrt(mid/r)) for r in ranks)
            if noOfCars < cars:
                left = mid + 1
            else:
                ans = mid 
                right = mid - 1
        return ans