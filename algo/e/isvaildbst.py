# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    # Constructor to create a new Node
    def __init__( self, data = 0):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def isValidBST( self, root: TreeNode ) -> bool:
        return True























# # iteratively, in-order traversal
# # O(n) time and O(n)+O(lgn) space
# def isValidBST(self, root):
#     stack, res = [], []
#     while True:
#         while root:
#             stack.append(root)
#             root = root.left
#         # if root is None or all the nodes have
#         # been traversed and have no confliction
#         if not stack:
#             return True
#         node = stack.pop()
#         # res stores the current values in in-order
#         # traversal order, node.val should larger than
#         # the last element in res
#         if res and node.val <= res[-1]:
#             return False
#         res.append(node.val)
#         root = node.right