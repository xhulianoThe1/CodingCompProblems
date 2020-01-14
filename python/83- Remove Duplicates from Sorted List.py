class Solution(object):
    def deleteDuplicates(self, head):
        arr = [] 
        while head is not None: 
            if head.val not in arr: 
                arr.append(head.val)            
            head = head.next 
        return self.linkedlistconvert(arr)
    def linkedlistconvert(self, l):
        curr = tmp = ListNode(0)
        for i in l:
            curr.next = ListNode(i)
            curr = curr.next
        return tmp.next    
