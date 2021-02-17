# Author: Abshar Mohammed Aslam, github.com/abxhr

import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [int(i) for i in list(str(n))]
        return(math.prod(n) - sum(n))
