from treenode import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        using BFS
        '''
        if not root: return root

        queue = deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        return root
