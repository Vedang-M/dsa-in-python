class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = [] 

        for curr_idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                ans[prev_idx] = curr_idx - prev_idx
            
            stack.append((curr_temp, curr_idx))

        return ans
