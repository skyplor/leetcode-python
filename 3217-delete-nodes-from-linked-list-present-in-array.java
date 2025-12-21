import java.util.*;

class DeleteNodesFromLinkedListPresentInArray {
    /**
     * Definition for singly-linked list.
     */
    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode modifiedList(int[] nums, ListNode head) {
        ListNode dummy = new ListNode(-1, head);
        ListNode prev = dummy;
        ListNode cur = head;
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            seen.add(num);
        }

        while (cur != null) {
            if (seen.contains(cur.val)) {
                prev.next = cur.next;
            } else {
                prev = cur;
            }
            cur = cur.next;
        }

        return dummy.next;
    }

    public static void main(String[] args) {

        DeleteNodesFromLinkedListPresentInArray sol = new DeleteNodesFromLinkedListPresentInArray();
        // To access the inner class ListNode, create it via the outer class instance
        ListNode testHead = sol.new ListNode(1, 
            sol.new ListNode(2, 
                sol.new ListNode(3, 
                    sol.new ListNode(4, 
                        sol.new ListNode(5)))));
        System.out.println("Output: " + sol.modifiedList(new int[] { 1, 2, 3 }, testHead));
    }
}
