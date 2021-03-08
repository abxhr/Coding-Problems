# Author: Abshar Mohammed Aslam, github.com/abxhr

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        f = True
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                f = False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                f = False
        elif carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False
