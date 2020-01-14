#Solution 1 

class Solution(object):
    def backspaceCompare(self, S, T):
        stack = [] 
        i = 0 
        while i < len(S): 
            if S[i] != '#': 
                stack.append(S[i])
                i+=1
            elif S[i] == "#" and len(stack) >= 1: 
                stack.pop() 
                i+=1 
            elif S[i] == '#' and len(stack) < 1: 
                i+=1 
        stack2 = [] 
        k = 0 
        while k < len(T): 
            if T[k] != '#': 
                stack2.append(T[k])
                k+=1
            elif T[k] == "#" and len(stack2) >= 1: 
                stack2.pop() 
                k+=1 
            elif T[k] == '#' and len(stack2) < 1: 
                k+=1 
        return stack == stack2
#Solution 2 
class Solution(object):
    def backspaceCompare(self, S, T):
        def compare(S): 
            stack = [] 
            i = 0 
            while i < len(S): 
                if S[i] != '#': 
                    stack.append(S[i])
                    i+=1
                elif S[i] == "#" and len(stack) >= 1: 
                    stack.pop() 
                    i+=1 
                elif S[i] == '#' and len(stack) < 1: 
                    i+=1 
            return stack
        return compare(S) == compare(T)
