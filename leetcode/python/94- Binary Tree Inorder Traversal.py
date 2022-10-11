class Solution(object):
    def inorderTraversal(self, root):
        arr = [] 
        if root:
            arr = self.inorderTraversal(root.left)
            arr.append(root.val) 
            arr = arr + self.inorderTraversal(root.right)
        return arr
        
        #Second Solution 
       '''
        class Solution(object):
    def inorderTraversal(self, root):
        if root: 
            return(self.inorderTraversal(root.left) + [root.val] +  self.inorderTraversal(root.right))
        else: 
            return [] 
          ''' 
