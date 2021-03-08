# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def interpret(self, command: str) -> str:
        return (command.replace('()','o')).replace('(al)','al')
