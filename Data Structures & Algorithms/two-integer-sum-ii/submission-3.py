class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Optimizing the solution for space complexity O(1) and time complexity O(n)
        tmp = []
        left = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                tmp.append(left+1)
                tmp.append(right+1)
                return tmp
            
            elif numbers[left]+numbers[right]>target:
                right-=1
            
            else:
                left+=1
        
        return tmp