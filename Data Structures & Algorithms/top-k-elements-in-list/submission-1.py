class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = dict()
        ans = []
        for i in nums:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i]+=1

        sorted_keys = sorted(d1, key= lambda x: d1[x])
        return sorted_keys[-k:]
