class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t)>len(s):
            return ""

        left = 0
        need = {}
        ans = ""
        for i in range(len(t)):
            if t[i] not in need:
                need[t[i]] = 1
            else:
                need[t[i]]+=1

        curr = {}
        best_len = float('inf')
        def win_valid(curr:dict, need:dict):
            for c in need:
                if curr.get(c, 0) < need[c]:
                    return False
            
            return True

        for right in range(len(s)):
            ch = s[right]

            if ch not in curr:
                curr[ch] = 1
            else:
                curr[ch]+=1

            while win_valid(curr, need):
                window_len = right - left + 1
                
                if window_len < best_len:
                    best_len = window_len
                    ans = s[left:right+1]

                curr[s[left]]-=1
                

                if curr[s[left]] == 0:
                    del curr[s[left]]
                
                left+=1 
        
        return ans