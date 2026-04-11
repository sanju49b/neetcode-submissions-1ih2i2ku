class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first+second)
            elif i == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first)
            elif i == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            elif i == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(second * first)
            
            else:
                stack.append(int(i))

        return stack[-1]
