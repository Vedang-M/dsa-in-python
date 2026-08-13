class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
        for n in nums:
            bits |= n # Bit wise OR
        return bits << len(nums)-1 #Left wise bit shift