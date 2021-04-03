# Author: Abshar Mohammed Aslam, github.com/abxhr

import time
class Foo:
    def __init__(self):
        self.f = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.f != 1:
            time.sleep(0.01)
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.f = 2

        
    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.f != 2:
            time.sleep(0.01)
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        
        