#Solution 1 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 9 and len(digits) ==1:
            return [1, 0]
        
        for i in reversed(range(len(digits))): 
            if digits[i] == 9 and digits[i-1] != 9: 
                digits[i] = 0 
                digits[i-1] +=1 
                break 
            elif digits[i] !=10 and digits[i] != 9: 
                digits[i] +=1 
                break 
            elif digits[i] ==10 and i!= 0 and digits[i-1] != 9: 
                digits[i] = 0 
                digits[i-1] += 1
                break 
            elif digits[i] == 10 and i == 0:
                digits[i] = 0 
                digits.insert(0, 1)
                break 
            elif digits[i] == 9 or (digits[i] ==10 and i!= 0 and digits[i-1] == 9): 
                digits[i] = 0 
                digits[i-1] +=1 
        return digits
 
#Solution 2 one-liner 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int(''.join(list(map(str, digits)))) + 1 )]
