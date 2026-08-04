class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp = nums1+nums2
        tmp = sorted(tmp)

        if len(tmp)%2!=0:
            return tmp[len(tmp)//2]
        
        else:
            return (tmp[len(tmp)//2]+tmp[len(tmp)//2 - 1])/2