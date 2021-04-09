# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        queue.append(root)
        output = []        
        
        while root and queue:
            current_nodes, next_level = [], []
            
            for node in queue:
                current_nodes.append(node.val)
                
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
                    
            output.append(current_nodes)
            queue = next_level
        
        return output
            
            