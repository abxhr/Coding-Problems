# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        count_letters = {}
        for i in chars:
            count_letters[i] = chars.count(i)
        for word in words:
            sum += len(word)
            for letter in word:
                if letter not in count_letters or count_letters[letter] < word.count(letter):
                    sum -= len(word)
                    break
        return sum