class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        maxi = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                curr_max = min(heights[i], heights[j])*abs(j-i)
                maxi = max(curr_max, maxi)

        return maxi
        