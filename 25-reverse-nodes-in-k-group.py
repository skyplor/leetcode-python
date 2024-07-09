from listnode import ListNode, toArray, generateListNodes
from typing import Optional

class Solution:
  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    '''
      we have a dummy node that points to the first node
      we have a counter that increments for each jump
      once we reach the Kth node, reverse the group.
      First node of the group will have its next pointer point to the next pointer of the Kth node
      last node of the previous group will point to the Kth node
    '''
    dummy = ListNode()
    dummy.next = current = group_head = head
    counter = 1
    prev = dummy
    while current:
      if counter == k:
        # do the reversal
        next_group_head = current.next
        current.next = None
        self.reverseList(group_head)
        group_head.next = next_group_head
        prev.next = current

        # reset
        prev = group_head
        group_head = current = next_group_head
        counter = 1
      else:
        current = current.next
        counter += 1

    return dummy.next
  
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
k = 3
output = sol.reverseKGroup(head, k)
print(f'head: {toArray(head)}\nk: {k}\noutput: {toArray(output)}')