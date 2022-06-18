# Author: Abshar Mohammed Aslam, github.com/abxhr

import math
lst = list(map(int, input().split()))
n = lst[0]
m = lst[1]
a = lst[2]
print(math.ceil(n/a) * math.ceil(m/a))
