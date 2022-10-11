class Solution(object):
    def mergeTwoLists(self, l1, l2):
        arr = []
        while l1:
            arr.append(l1.val)
            l1 = l1.next
        arr2 = []
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        return self.link(sorted(arr+arr2)) 
        
    def link(self, link): 
        curr= tmp = ListNode(0)
        for i in link: 
            curr.next = ListNode(i)
            curr = curr.next 
        return tmp.next 
