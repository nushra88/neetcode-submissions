class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = []
        S = []

        for i in strs:
            A.append(["".join(sorted(i)), i])
            S.append("".join(sorted(i)))
        
        S = set(S)
        group = {}

        for i in S:
            group[i] = []
            for j in A:
                if j[0] == i:
                    group[i].append(j[1])
        
        return(list(group.values()))
