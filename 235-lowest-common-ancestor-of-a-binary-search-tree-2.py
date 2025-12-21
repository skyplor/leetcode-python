from treenode import TreeNode, createBTree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        the common ancestor will always be the node where the split happens
        so we compare p_val and q_val with the cur_val. if (p_val < cur_val and q_val > cur_val) or (q_val < cur_val and p_val > cur_val)
        then cur node is the ancestor
        if p_val == cur_val then p is the ancestor
        if q_val == cur_val then q is the ancestor
        using DFS, we first check the root node. if both p and q belongs to same side, then we go down the tree
        '''
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur


sol = Solution()
# root = createBTree([6,2,8,0,4,7,9,None,None,3,5], 0)
# p = root.left
# q = root.left.right
root = createBTree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 0)
p = root.left
q = root.right.left
output = sol.lowestCommonAncestor(root, p, q)
print(f'root: {root}\np: {p}\nq: {q}\noutput: {output}')
