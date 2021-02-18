# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        sieve = [0] * n
        sieve[0] = 1
        sieve[1] = 1
        
        to = int(math.sqrt(n)) + 1
        for i in range(2, to):
            j = 2
            while (i*j) < n:
                sieve[i*j] = 1
                j += 1
        return len([num for num in sieve if num == 0])