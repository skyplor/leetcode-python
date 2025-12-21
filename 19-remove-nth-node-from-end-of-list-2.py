from typing import Optional
from listnode import ListNode, toArray, generateListNodes


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        2 pointers, 1 is fast pointer, another is slow pointer.
        We move the fast pointer n times, then start to move the slow pointer
        once fast pointer hit a None, we update the node of slow pointer's next to point to next.next
        '''
        prev = dummy = ListNode()
        dummy.next = slow = fast = head
        counter = 1
        while counter < n:
            fast = fast.next
            counter += 1
            
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
            
        prev.next = slow.next
        return dummy.next


sol = Solution()
# head = generateListNodes([1, 2, 3, 4])
# head = generateListNodes([1])
head = generateListNodes([1, 2])
print(f'head: {toArray(head)}')
new_head = sol.removeNthFromEnd(head, 2)
print(f'head: {toArray(new_head)}')
