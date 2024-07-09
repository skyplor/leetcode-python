from typing import Optional
from listnode import ListNode, toArray, generateListNodes

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    '''
    First solution:
      Go through the listnode, calculate how many nodes are there until end of list
      Go through the listnode again, this time once we hit len(list) - n, we remove the node and set the current.next as current.next.next
    Second solution (1-pass):
      Use 2 pointers, 1 starts earlier. Once it moves n times, we start moving the 2nd pointer. once pointer 1 reach the end, we are sure that 2nd pointer is at the nth node
      We also have a `prev` pointer that points to the previous node so we can set the next node correctly
    '''
    
    p_a = p_b = head
    prev = None
    counter = 1
    while counter < n and p_a:
      p_a = p_a.next
      counter += 1
    while p_a and p_a.next and p_b:
      p_a = p_a.next
      prev = p_b
      p_b = p_b.next

    if not prev and p_b: return p_b.next
    if not prev: return None

    prev.next = prev.next.next
    
    return head
    
  
sol = Solution()
# head = generateListNodes([1, 2, 3, 4])
# head = generateListNodes([1])
head = generateListNodes([1, 2])
print(f'head: {toArray(head)}')
new_head = sol.removeNthFromEnd(head, 2)
print(f'head: {toArray(new_head)}')
  
