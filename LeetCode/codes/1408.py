# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        array = ' '.join(words)
        return [i for i in words if array.count(i) > 1]