class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:
    '''
      Need some kind of pointer to the least recently used entry
      Need to be able to push in an entry
      Each time we push in an entry, it will represent the most recently used entry
      pointer to represent most recently used
      left (LRU) and right pointer (MRU)
      get
          if unable to find the key in hashmap, return -1
          each time we call get(), we can move the key to the MRU
          since get() has to be O(1), use a hash map to store the key and value will be the node itself
      put
          each time we call put(), we update the value and move the key to the MRU (can potentially use the get function)
          if capacity exceeds (using the size of the hashmap), we remove a node from the LRU and remove it from the hashmap
      represent each entry in the cache as a node that has a prev and next pointer to other nodes
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left
        self.hash = {}

    def remove_node(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
        del self.hash[node.key]

    def insert_node(self, node: Node) -> None:
        mru_node = self.right.prev
        mru_node.next = node
        self.right.prev = node
        node.next, node.prev = self.right, mru_node
        self.hash[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        node = self.hash[key]
        self.remove_node(node)
        self.insert_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            node = Node(key, value)
            self.insert_node(node)
        else:
            node = self.hash[key]
            node.value = value
            self.get(key)

        if len(self.hash) > self.capacity:
            self.remove_node(self.left.next)


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
