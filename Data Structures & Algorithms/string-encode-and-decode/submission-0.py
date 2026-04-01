class Solution:
    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r += str(len(s)) + "!" + s
        return r

    def decode(self, s: str) -> List[str]:
        res,i = [],0
        while i < len(s):
            j = i
            while s[j] != "!":
                j +=1
            length = int(s[i:j]) #4
            res.append(s[j+1:length+j+1])
            i = length + j +1
        return res

