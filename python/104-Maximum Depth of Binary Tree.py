class Solution(object):
    def maxDepth(self, root):
        #Base Case 
        if root == None: 
            return 0
        else: 
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 
