class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 0

        while left<=right:
            mid = (left+right)//2
            count = 0

            for pile in piles:
                hour = pile//mid

                if pile%mid!=0:
                    count+=1
                
                count+=hour

            if count<=h:
                ans = mid
                right = mid-1
                
            if count>h:
                left = mid+1

        
        return ans