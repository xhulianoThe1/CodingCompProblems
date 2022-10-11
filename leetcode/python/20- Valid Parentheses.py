class Solution(object):
    def isValid(self, s):
        stack = [] 
        for i in s: 
            if i == '(' or i == '{' or i == '[': 
                stack.append(i)
            elif i == ')' and len(stack) != 0 and stack[-1] == '(': 
                stack.pop()
            elif i == '}' and len(stack) != 0 and stack[-1] == '{': 
                stack.pop()
            elif i == ']' and len(stack) != 0 and stack[-1] == '[': 
                stack.pop()
             
        if len(s) % 2 != 0: 
            return False 
        else: 
            return len(stack) == 0
            
             
        
             
                
                
                
                
                
                
