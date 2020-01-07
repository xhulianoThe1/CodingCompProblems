class Solution(object):
    def getDecimalValue(self, head):
        s = " "
        while head: 
            s += str(head.val)
            head = head.next
        s1 = "".join(map(str, s))
        return int(s1, 2)
