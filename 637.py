# https://leetcode.com/problems/average-of-levels-in-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        tobeTraversed = [root]
        
        while(tobeTraversed):
            sum = 0
            length = 0
            nextLevel = []
            
            while(tobeTraversed):
                node = tobeTraversed.pop(0)
                sum += node.val
                length += 1
                if(node.left):
                    nextLevel.append(node.left)
                if(node.right):
                    nextLevel.append(node.right)
            tobeTraversed = nextLevel
            result.append(sum/length)                
            
        return result
            
