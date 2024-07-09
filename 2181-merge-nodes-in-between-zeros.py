from listnode import ListNode, toArray, generateListNodes
from typing import Optional

class Solution:
  def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Using 1 ptr to go through each node
    using 2 variables to represent nodes (res, cur)
    return res node
    '''
    ptr = head.next
    dummy = ListNode()
    cur = ListNode(0)
    dummy.next = cur
    while ptr:
      if ptr.val != 0:
        cur.val += ptr.val
      else:
        if ptr.next:
          newNode = ListNode()
          cur.next = newNode
          cur = cur.next
      ptr = ptr.next
    
    return dummy.next

sol = Solution()
# head = generateListNodes([0,3,1,0,4,5,2,0])
head = generateListNodes([0,1,0,3,0,2,2,0])
# print(f'output: {toArray(head)}')
print(f'output: {toArray(sol.mergeNodes(head))}')