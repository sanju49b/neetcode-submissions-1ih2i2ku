class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # steps involved
        # first: pair it and sort it in reverse order
        # define an empty stack
        stack = []
        pairs =[[p,s] for p,s in zip(position,speed)]
        sorted_pairs = sorted(pairs,reverse=True)
        for pos,speed in sorted_pairs:
            stack.append((target-pos)/speed)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


