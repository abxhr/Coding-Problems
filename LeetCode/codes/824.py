# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = list('aeiouAEIOU')
        new_s = ''
        c = 1
        for word in S.split():
            if word == ' ':
                new_s += word
            else:
                if word[0] in vowels:
                    word += 'ma'
                else:
                    word = word[1:] + word[0] + 'ma'
                word += 'a'*c
                new_s += word
            new_s += ' '
            c += 1
        return new_s[:-1]
