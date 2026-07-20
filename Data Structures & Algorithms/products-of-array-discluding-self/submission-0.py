class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        for i in range(len(nums)):
            pro *=nums[i]
        
        ans = []
        pro2 = 1
        for i in range(len(nums)):
            if nums[i]==0:
                tmp=nums.copy()
                tmp = tmp[:i] + tmp[i+1:]
                for j in range(len(tmp)):
                    pro2*=tmp[j]
                print(pro2)
                ans.append(pro2)
            
            else:
                ans.append(pro//nums[i])

        return ans