class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lst = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for word in words:
            word_set = set(word.lower())
            if word_set.intersection(row1) == word_set:
                lst.append(word)
            elif word_set.intersection(row2) == word_set:
                lst.append(word)
            elif word_set.intersection(row3) == word_set:
                lst.append(word)
        return lst
