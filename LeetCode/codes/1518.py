# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while (numBottles >= numExchange):
            count += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)            
        return count