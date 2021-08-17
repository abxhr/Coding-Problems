# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        mlist = []
        for word in words:
            morse = ''
            for l in word:
                val = ord(l)-97
                morse += alpha[val]
            mlist.append(morse)
        return(len(set(mlist)))
