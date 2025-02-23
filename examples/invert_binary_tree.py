# Given the root of a binary tree, invert the tree, and return its root.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None: return None

    aux = root.left
    root.left = root.right
    root.right = aux

    # root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

print(invertTree([4,2,7,1,3,6,9]))
