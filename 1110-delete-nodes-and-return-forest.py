from treenode import TreeNode, createBTree
from typing import List, Optional
from collections import deque

class Solution:
  def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    '''
    use 2 variables parents set and children hashmap (child -> parent)
    whenever we delete a node, we remove that mapping
    1. 1 has at least a child, add 1 to parents, Add 2 and 3 to children (2 -> 1, 3 -> 1)
    2. 2 has at least a child, add 2 to parents, Add 4 and 5 to children (4 -> 2, 5 -> 2)
    3. 3 has at least a child, add 3 to parents, Add 6 and 7 to children (6 -> 3, 7 -> 3)
    4. 4 has no child
    5. 5 has no child
    6. 6 has no child
    7. 7 has no child
    8. remove 3 from parent and child if exist (parents: [1, 2], children: {2: 1, 4: 2, 5: 2, 6: 3, 7: 3})
    9. remove 5 from parent and child if exist (parents: [1, 2], children: {2: 1, 4: 2, 6: 3, 7: 3})
    10. loop through each children and get the base parent and set that as the parent
    11. {2: 1, 4: 1, 6: 3, 7: 3}
    12. loop through children, If child's parent is not in parent, add into parent, if child's parent is in parent and child is in parent, remove child from parent
    13. a: parents: [1] (delete 2 from parent)
    13. b: parents: [1, 6]
    13. c: parents: [1, 6, 7]
    '''
    parents = set()
    children = {}
    nodesMapping = {}
    # populate the parents and children variables
    queue = deque([root])
    while queue:
      cur = queue.popleft()
      nodesMapping[cur.val] = cur
      if cur.left or cur.right:
        parents.add(cur.val)
        if cur.left:
          children[cur.left.val] = cur.val
          queue.append(cur.left)
        if cur.right:
          children[cur.right.val] = cur.val
          queue.append(cur.right)

    # removal
    for item in to_delete:
      if item in parents:
        # might need to set value as parents instead. We then have a mapping of value to nodes
        parents.remove(item)
      if item in children:
        # delete the actual node from parent
        parentVal = children[item]
        parentNode = nodesMapping[parentVal]
        if parentNode.left and parentNode.left.val == item:
          parentNode.left = None
        elif parentNode.right and parentNode.right.val == item:
          parentNode.right = None
        del children[item]
    
    # rebase parent of child
    for childVal,parentVal in children.items():
      # get base parent
      while parentVal in children:
        newParentVal = children[parentVal]
        if newParentVal in parents:
          parentVal = newParentVal
        else:
          break
      children[childVal] = parentVal
    # update parents
    for childVal,parentVal in children.items():
      if parentVal not in parents:
        parents.add(childVal)
      else:
        # if child in parents, remove child from parents
        if childVal in parents:
          parents.remove(childVal)
    res = []
    for item in parents:
      res.append(nodesMapping[item])
    return res

sol = Solution()
# root = createBTree([1,2,3,4,5,6,7])
# to_delete = [3,5]
# root = createBTree([1,2,4,None,3])
# to_delete = [3]
root = createBTree([1,2,3,None,None,None,4])
to_delete = [2,1]
print(f'output: {sol.delNodes(root, to_delete)}')