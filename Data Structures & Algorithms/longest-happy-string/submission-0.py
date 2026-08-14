class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        
        while True:
        
            scores = {'a': a, 'b': b, 'c': c}
            
            ranking = sorted(scores, key=scores.get, reverse=True)
            added = False
            
            for char in ranking:
                if scores[char] == 0:
                    break
                
                if s[-2:] == char * 2:
                    continue  
                s += char

            
                if char == 'a': 
                    a -= 1
                elif char == 'b': 
                    b -= 1
                elif char == 'c': 
                    c -= 1
                
                added = True
                break

            if not added:
                break
                
        return s
