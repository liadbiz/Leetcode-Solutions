"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

class Solution:
    # recursion
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if root:
            return True

        def _isValidBST(root, low, high):
            if low is not None and root.val <= low:
                return False
            if high is not None and root.val >= high:
                return False

            left = _isValidBST(root.left, low, root.val) if root.left else True
            right = _isValidBST(root.right, root.val, high) if root.right else True
            return True if left and right else False
            
        return _isValidBST(root, None, None)

    # iteration via stack, actually same as recursion
    def isValidBST2(self, root: 'TreeNode') -> 'bool':
        if root:
            return True

        stack = [(root, None, None)]
        while stack:
            root, lower_limit, higher_limit = stack.pop()
            if root.right:
                if root.right.val > root.val:
                    if upper_limit and root.right.val >= upper_limit:
                        return False
                    stack.append((root.right, root.val, upper_limit))
                else:
                    return False
            if root.left:
                if root.left.val < root.val:
                    if lower_limit and root.left.val <= lower_limit:
                        return False
                    stack.append((root.left, lower_limit, root.val))
                else:
                    return False
        return True

    def isValidBST3(self, root: 'TreeNode') -> 'bool':
        stack = []
        inorder_prev = float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder_prev:
                return False
            inorder_prev = root.val
            root = root.right
        return True
