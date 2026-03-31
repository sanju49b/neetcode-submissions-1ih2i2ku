class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            x = ''.join(sorted(word))
            if x in seen:
                seen[x].append(word)
            else:
                seen[x] = [word]
        return list(seen.values())
        