from typing import Optional
from node import Node

class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    '''
    Using 2-pass, hashmap
    Step 1: Create clone of each node and a hashmap of old node -> new node
    Step 2: go through and link each of the new nodes to the next and random node using the hashmap
    '''
    current = head
    hashmap = {None: None}
    while current:
      node = Node(current.val)
      hashmap[current] = node
      current = current.next
    current = head
    while current:
      node = hashmap[current]
      next_node = hashmap[current.next]
      random_node = hashmap[current.random]
      node.next = next_node
      node.random = random_node
      current = current.next

    return hashmap[head]

sol = Solution()
node5 = Node(1)
node4 = Node(10, node5)
node3 = Node(11, node4)
node2 = Node(13, node3)
node1 = Node(7, node2)

node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1