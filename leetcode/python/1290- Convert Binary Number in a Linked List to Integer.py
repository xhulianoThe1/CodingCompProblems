class Solution(object):
    def getDecimalValue(self, head):
        s = " "
        while head: 
            s += str(head.val)
            head = head.next
        return int(s, 2)
