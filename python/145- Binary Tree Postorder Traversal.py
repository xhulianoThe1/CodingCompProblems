class Solution(object):
    def postorderTraversal(self, root):
        arr = []
        if root: 
            arr = self.postorderTraversal(root.left)
            arr = arr + self.postorderTraversal(root.right)
            arr.append(root.val)
        return arr
   

''' Second Solution 
class Solution(object):
    def postorderTraversal(self, root):
        if root: 
            return (self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]) 
        else: 
            return []         
'''
