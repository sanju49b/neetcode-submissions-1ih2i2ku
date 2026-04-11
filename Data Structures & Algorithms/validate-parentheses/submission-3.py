class Solution:
    def isValid(self, s: str) -> bool:
        # why do we need to stack ds
        # the reason for using stack in here we are always popping the last element so we need stack as stak is lifo
        closetoopen = {"]":"[","}":"{",")":"("}
        stack = []
        for i in s:

            #this means this is a closing bracket
            if i in closetoopen:
                if stack and stack[-1] == closetoopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if stack:
            return False
        else:
            return True