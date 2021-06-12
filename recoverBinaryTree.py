# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        self.first = TreeNode()
        self.last = TreeNode()
        self.flag = False
        
    def recoverTree(self, root: TreeNode) -> None:
        if not root:
            return None
        print(self.flag)
        self.inorder(root)
        self.first.val, self.last.val = self.last.val, self.first.val
    
    def inorder(self,root):
        #base
        if root is None:
            return
        
        #Logic
        self.inorder(root.left);
        # print(self.prev.val,root.val)
        if self.prev is not None and self.prev.val>=root.val:
            if self.flag == False:
                # print(self.prev.val,root.val)
                self.first= self.prev
                self.last = root
                self.flag = True
            else:
                self.last = root
        self.prev = root
        self.inorder(root.right)
        
        
        
