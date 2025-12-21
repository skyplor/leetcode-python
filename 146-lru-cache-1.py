

class Node:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = self.next = None

class LRUCache:
  def __init__(self, capacity: int):
    self.cache = {}
    self.cap = capacity
    self.left, self.right = Node(0, 0), Node(0, 0)
    self.left.next, self.right.prev = self.right, self.left
    
  # insert to right
  def insertNode(self, node):
    mru_node = self.right.prev
    mru_node.next = node
    node.prev, node.next = mru_node, self.right
    self.right.prev = node
  
  # remove from left
  def removeNode(self, node):
    prev_node, next_node = node.prev, node.next
    prev_node.next = next_node
    next_node.prev = prev_node

  def get(self, key: int) -> int:
    if key in self.cache:
      node = self.cache[key]
      self.removeNode(node)
      self.insertNode(node)
      return node.val
    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      node = self.cache[key]
      self.removeNode(node)

    node = Node(key, value)
    self.cache[key] = node
    self.insertNode(node)

    if len(self.cache) > self.cap:
      lru_node = self.left.next
      self.removeNode(lru_node)
      del self.cache[lru_node.key]

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