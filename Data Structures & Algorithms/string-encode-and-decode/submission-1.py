class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        j = ""
        i = 0
        while i<len(s):
            while s[i] != "#":
                j += s[i]
                i += 1
            a = int(j)
            res.append(s[i+1:i+a+1])
            i = i+1+a
            j = ""
        return res
