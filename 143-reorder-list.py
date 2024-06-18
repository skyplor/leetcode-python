from typing import Optional
from listnode import ListNode
from listnode_utils import toArray, generateListNodes

class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    if we allow o(n) memory, then we can use an extra array to hold onto all the nodes
    then we just use the index of the array to rebuild the list
    if we are only allowed to have o(1) memory, then we can do the following:
    traverse through and get the 2nd half of the list (we can use fast-slow pointers method)
    the 2nd half of the list will be the slow-pointer's next node
    E.g
    if 5 nodes
    step 1: s = 1, f = 2
    step 2: s = 2, f = 4 (2 + 2)
    step 3: s = 3, f = null (4 + 2)
    2nd half is at node 4 (node 3's next)
    
    if 4 nodes
    step 1: s = 1, f = 2
    step 2: s = 2, f = 4 (2 + 2)
    2nd half is at node 3 (node 2's next)
    
    Next, we reverse the 2nd half of the nodes
    Next, using the 2 pointers to the head of each half, we intersect them
    """

    if not (head or head.next): return

    slow, fast = head, head.next
    # step 1, find the 2 halfs
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    second_head = slow.next
    slow.next = None
    first = head
    # Step 2: reverse list2
    second = self.reverseList(second_head)
    # Step 3: intersect first and second
    while second:
      next_first, next_second = first.next, second.next
      first.next = second
      second.next = next_first
      first, second = next_first, next_second
    
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current, prev = head, None
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node

    return prev
  
sol = Solution()
head = generateListNodes([1, 2, 3, 4, 5])
input = toArray(head)
sol.reorderList(head)
output = toArray(head)
# output = sol.toArray(sol.reverseList(head))
print(f'input: {input}\noutput: {output}')
  