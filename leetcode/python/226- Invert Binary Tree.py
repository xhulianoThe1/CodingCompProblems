class Solution(object):
    def invertTree(self, root):
        if root is None: 
            return root 
        else:
            right = self.invertTree(root.left)
            left = self.invertTree(root.right)
            root.left = left
            root.right = right
        return root  
