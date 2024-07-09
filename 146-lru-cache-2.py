class Node:
  def __init__(self, key: int, val: int):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None

class LRUCache:
  '''
  get -> use hashmap
  some way to remove least recently used node in constant time, and a way to add most recently used node
  2 pointers to point to least and most recently used
  use linkedlist for o(1) removal
  left->node1->node2->node3->right
  '''
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.hash = {}
    self.left = Node(-1, -1)
    self.right = Node(-1, -1)
    self.left.next, self.right.prev = self.right, self.left
  
  def removeLruNode(self) -> Node:
    lruNode = self.left.next
    self.left.next = lruNode.next
    return lruNode
  
  def removeNode(self, node: Node) -> None:
    nextNode = node.next
    prevNode = node.prev
    prevNode.next = nextNode
    nextNode.prev = prevNode
  
  def addNode(self, node: Node) -> None:
    mruNode = self.right.prev
    mruNode.next = node
    node.prev, node.next = mruNode, self.right
    self.right.prev = node

  def get(self, key: int) -> int:
    if key in self.hash:
      node = self.hash[key]
      self.removeNode(node)
      self.addNode(node)
      return node.val

    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.hash:
      node = self.hash[key]
      node.val = value
      self.removeNode(node)
    else:
      node = Node(key, value)
      # check for capacity. if exceed, then we remove LRU node
      if self.capacity == len(self.hash):
        nodeToRemove = self.removeLruNode()
        if nodeToRemove.key in self.hash:
          del self.hash[nodeToRemove.key]
      self.hash[key] = node
    self.addNode(node)

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))