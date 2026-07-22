class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        for i in s:
            if (i==')' or i==']' or i=='}') and not my_stack:
                return False
            
            if i=='(' or i=='{' or i=='[':
                my_stack.append(i)
            
            if (i==')'and my_stack[-1]=='(') or (i==']'and my_stack[-1]=='[') or (i=='}'and my_stack[-1]=='{'):
                my_stack.pop()
            
            elif (i==')'and my_stack[-1]!='(') or (i==']'and my_stack[-1]!='[') or (i=='}'and my_stack[-1]!='{'):
                return False
            
        
        return not my_stack
