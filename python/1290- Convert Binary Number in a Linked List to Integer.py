class Solution(object):
    def getDecimalValue(self, head):
        arr =[] 
        while head: 
            arr.append(head.val)
            head = head.next
        s = "".join(map(str, arr))
        return int(s, 2)
