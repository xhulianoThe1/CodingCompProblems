class Solution(object):
    def calPoints(self, ops):
        arr, s = [], 0
        for i in range(len(ops)):       
            if ops[i] != 'C' and ops[i] != 'D' and ops[i] != '+': 
                arr.append(int(ops[i]))
            elif ops[i] == 'C': 
                del arr[-1]
            elif ops[i] == 'D': 
                arr.append(arr[-1]*2)
            elif ops[i] == '+': 
                arr.append(arr[-1] + arr[-2])
        return sum(arr)
