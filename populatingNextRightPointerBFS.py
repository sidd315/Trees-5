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
        
        q = list()
        q.append(root)
        while q:
            size = len(q)
            prev = q.pop(0)
            if prev.left is not None:
                q.append(prev.left)
                q.append(prev.right)
            for i in range(size-1):
                curr = q.pop(0)
                prev.next = curr
                if curr.left is not None:
                    q.append(curr.left)
                    q.append(curr.right)
                prev = curr
        return root
            
        
