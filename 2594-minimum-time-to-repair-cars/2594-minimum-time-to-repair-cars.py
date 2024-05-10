class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        ans = math.inf
        left, right = 0, max(ranks)*cars*cars
        while left<=right:
            mid = (left+right)//2
            noOfCars = 0
            for r in ranks:
                car = int((mid//r)**0.5)
                noOfCars += car
    
            if noOfCars < cars:
                left = mid + 1
            else:
                ans = min(ans, mid) 
                right = mid - 1
        return ans