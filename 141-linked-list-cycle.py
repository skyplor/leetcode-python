from typing import Optional
from listnode import ListNode, toArray, generateListNodes

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    '''
      using o(n) memory, we can create a hashmap and add each node as a key.
      each time we go to the next node, if it exists in hashmap as a key, then we can return true and exit
      
      another way is to have o(1) memory.
      We can use the fast and slow pointers.
      If there is a cycle, at some point, the pointers will meet and once the pointers are equal, we exit
    '''
    # Memory: o(n)
    # hashset = set()
    # current = head
    # while current:
    #   if current in hashset:
    #     return True
    #   hashset.add(current)
    #   current = current.next
    # return False
    #
    # Memory: o(1)
    fast = slow = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if fast == slow:
        return True
      
    return False
    
  
sol = Solution()
head = generateListNodes([3, 2, 0, -4])
node2 = head.next
node4 = head.next.next.next
node4.next = node2
print(sol.hasCycle(head))