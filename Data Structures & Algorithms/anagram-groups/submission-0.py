class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = dict()
        for i in range(len(strs)):
            tmp = "".join(sorted(strs[i]))
            if tmp not in d1:
                d1[tmp] = [strs[i]]
            
            else:
                d1[tmp].append(strs[i])

        return list(d1.values())

        