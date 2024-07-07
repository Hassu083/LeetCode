class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        full = numBottles // numExchange
        empty = numBottles - full * numExchange
        while full:
            ans += full
            empty += full
            full = empty // numExchange
            empty = empty - full * numExchange
        return ans