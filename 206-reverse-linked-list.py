from typing import Optional
from listnode import ListNode, toArray, generateListNodes

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    current, prev = head, None
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    return prev
  
sol = Solution()
head = generateListNodes([1, 2, 3])
input = toArray(head)
output = sol.reverseList(head)
print(f'input: {input}\noutput:{toArray(output)}')