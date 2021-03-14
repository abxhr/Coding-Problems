# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        inTruck = 0
        boxes_in_truck = 0
        for boxes, units in boxTypes:
            boxes_can_fit = min(truckSize, boxes)
            truckSize -= boxes_can_fit
            inTruck += boxes_can_fit * units
            if truckSize == 0:
                return inTruck
        return inTruck