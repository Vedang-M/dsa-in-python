class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        tmp = set()
        for i in nums:
            if i>0:
                tmp.add(i)
        
        for i in range(1, len(tmp)+2):
            if i not in tmp:
                return i