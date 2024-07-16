from typing import Optional
from treenode import TreeNode, createBTree, drawtree
from collections import deque

class Solution:
  def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    '''
    using a graph so we can do BFS for the shortest path from one node to the other node
    to build this graph, we need to be able to traverse from child to parent as well and we need to store some kind of direction
    using dfs to get the startValue
    using bfs and record the path to the destValue
    '''
    parent_map = {}
    start_node = self.find_start_node(root, startValue)
    if not start_node:
      return ''

    self.populate_parent_map(root, parent_map)
    queue = deque([start_node])
    path_tracker = {}
    visited = set([start_node])
    # to visit adj nodes from current node, we need to get parent node from parent_map and get the child nodes from cur.left and cur.right
    while queue:
      cur = queue.popleft()
      if cur.val == destValue:
        return self.backtrack_path(cur, path_tracker)

      if cur.val in parent_map:
        parent = parent_map[cur.val]
        if parent not in visited:
          queue.append(parent)
          path_tracker[parent] = (cur, 'U')
          visited.add(parent)

      if cur.left and cur.left not in visited:
        left_child = cur.left
        queue.append(left_child)
        path_tracker[left_child] = (cur, 'L')
        visited.add(left_child)
      if cur.right and cur.right not in visited:
        right_child = cur.right
        queue.append(right_child)
        path_tracker[right_child] = (cur, 'R')
        visited.add(right_child)

    return ''

  def find_start_node(self, root: TreeNode, startValue: int) -> Optional[TreeNode]:
    stack = [root]
    while stack:
      cur = stack.pop()
      if not cur:
        continue
      if cur.val == startValue:
        return cur
      stack.append(cur.left)
      stack.append(cur.right)

    return None

  def populate_parent_map(self, root: TreeNode, parent_map):
    queue = deque([root])
    while queue:
      cur = queue.popleft()
      if not cur:
        continue
      if cur.left and cur.left.val not in parent_map:
        parent_map[cur.left.val] = cur
      if cur.right and cur.right.val not in parent_map:
        parent_map[cur.right.val] = cur

      queue.append(cur.left)
      queue.append(cur.right)

  def backtrack_path(self, node: TreeNode, path_tracker) -> str:
    path = []
    while node in path_tracker:
      node, p = path_tracker[node]
      path.append(p)

    path.reverse()
    return ''.join(path)

sol = Solution()
root = createBTree([5,1,2,3,None,6,4])
startValue = 3
destValue = 6
print(f'output: {sol.getDirections(root, startValue, destValue)}')