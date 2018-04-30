# 538. Convert BST to Greater Tree

class Solution(object):
    def convertBST(self, root):
        self.val = 0
        def visit(root):
            if root:
                visit(root.right)
                root.val += self.val
                self.val = root.val
                visit(root.left)
        visit(root)
        return root