class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we are combining 2 lists of position and speed into one pair
        pairs = [[pos,spd] for pos,spd in zip(position,speed)]
        soreted_pairs = sorted(pairs,reverse=True)
        stack = []
        # process each pair
        for pos,spd in soreted_pairs:
            stack.append((target-pos)/spd)
            if len(stack) >=2 and stack [-1] <=stack[-2]:
                stack.pop()
        return len(stack)