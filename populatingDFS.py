"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        self.helper(root.left, root.right)
        return root
    
    def helper(self, left, right):
        #base
        if left is None:
            return None
        #logic
        left.next = right
        self.helper(left.left, left.right)
        self.helper(left.right, right.left)
        self.helper(right.left, right.right)
        
        
