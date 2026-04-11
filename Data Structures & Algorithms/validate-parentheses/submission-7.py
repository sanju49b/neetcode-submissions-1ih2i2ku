class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for b in s:
            if b in mapper:
                if stack and stack[-1] == mapper[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return len(stack) == 0
