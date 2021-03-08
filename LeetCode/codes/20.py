# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []    
        for i in s: 
            if(i=="(" or i=="{" or i=="["):
                stack.append(i)       
            else:            
                if(len(stack)>0):
                    c=stack.pop()     
                else:
                    return False         
                if not((i=="}" and c=="{") or(i==")" and c=="(") or (i=="]" and c=="[")):                
                    return False    
        if(len(stack)>0):
            return False    
        return True