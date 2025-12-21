from treenode import TreeNode, createBTree, drawtree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        We will use recursion here. Because we have this constraint: p and q will always exist, that means we can return either value if it's found first and don't need to continue to go down the subtree as the node will be the LCA.
        We then need to try and find the other value by going down the other subtree. If a node has 2 values returned from it's left and right subtree, that means this node is the LCA. If node only has 1 value returned, that means that value is the LCA
        base case is if root is empty, then we return None
        if root is the value, then we return the root
        otherwise, continue down both left and right children
        '''

        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left_node = right_node = None
        if root.left:
            left_node = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right_node = self.lowestCommonAncestor(root.right, p, q)

        if left_node and right_node:
            return root

        return left_node or right_node


sol = Solution()
root = createBTree([5, 4, 6, 1, 8, 3, 7, None, None, 9, 10])
# drawtree(root)
p = root.left
q = root.left.right.right
output = sol.lowestCommonAncestor(root, p, q)
print(f'output: {output}')
