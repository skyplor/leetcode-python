from treenode import TreeNode, createBTree, drawtree
class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    '''
    We will use preorder traversal and append nulls to leaf nodes
    '''
    res = []
    def dfs(cur):
      if not cur:
        res.append('null')
        return
      
      res.append(str(cur.val))
      dfs(cur.left)
      dfs(cur.right)
      
    dfs(root)
    return ','.join(res)
    

  def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    array = data.split(',')
    i = 0
    def dfs():
      nonlocal i
      if array[i] == 'null':
        i += 1
        return None
      
      node = TreeNode(int(array[i]))
      i += 1
      node.left = dfs()
      node.right = dfs()
      return node
      
    return dfs()      
    
ser = Codec()
deser = Codec()
root = createBTree([1,2,3,None, None, 4,5])
serialized = ser.serialize(root)
print(f'serialized: {serialized}')
drawtree(deser.deserialize(serialized))