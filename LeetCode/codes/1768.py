# Author: Abshar Mohammed Aslan, github.com/abxhr

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        chk = 1
        i1 = 0
        i2 = 0
        new_word = ''
        for i in range(len(word1) + len(word2)):
            if chk:
                if i1 < len(word1):
                    new_word += word1[i1]
                    i1 += 1
                    chk = 0
                else:
                    new_word += word2[i2:]
                    break
            else:
                if i2 < len(word2):
                    new_word += word2[i2]
                    i2 += 1
                    chk = 1
                else:
                    new_word += word1[i1:]
                    break
        return new_word
