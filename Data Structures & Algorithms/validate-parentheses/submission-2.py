class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(","]":"[","}":"{"}
        stack=[]
        for c in s:
            if c in hashmap.keys():
                #if this is for closing bracket
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True