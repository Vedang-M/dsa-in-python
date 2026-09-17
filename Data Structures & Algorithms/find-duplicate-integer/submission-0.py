class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst = set()
        for i in nums:
            if i not in lst:
                lst.add(i)
            
            else:
                return i