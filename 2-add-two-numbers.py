from listnode import ListNode
from listnode_utils import toArray, generateListNodes
from typing import Optional

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    carry, loop as long as l1 OR l2 is not null. If either one is null, treat the number as 0
    at the end, if there is a carry bit (> 0), create a node for that and link the last node to this carry node
    '''
    carry = 0
    c1, c2 = l1, l2
    res = ListNode()
    prev = None
    while c1 or c2:
      c1_num = c1.val if c1 else 0
      c2_num = c2.val if c2 else 0
      sum = carry + c1_num + c2_num
      val = sum if sum < 10 else sum - 10
      carry = sum // 10
      node = ListNode(val)
      if prev:
        prev.next = node
      else:
        res.next = node
      prev = node
      if c1:
        c1 = c1.next
      if c2:
        c2 = c2.next
    if carry > 0:
      carry_node = ListNode(carry)
      prev.next = carry_node

    return res.next

sol = Solution()
l1 = generateListNodes([2, 4, 3])
l2 = generateListNodes([5, 6, 4])
output = sol.addTwoNumbers(l1, l2)
print(f'inputs: {toArray(l1)}, {toArray(l2)}\noutput: {toArray(output)}')