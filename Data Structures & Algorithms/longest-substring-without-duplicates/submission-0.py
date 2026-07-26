class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = len(s)-1
        count = 0
        max_count = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                count+=1
            
            else:
                while s[left]!=s[right]:
                    seen.remove(s[left])
                    left+=1
                seen.remove(s[left])
                left+=1

                seen.add(s[right])
                count = right-left+1
        
            max_count = max(max_count, count)

        return max_count