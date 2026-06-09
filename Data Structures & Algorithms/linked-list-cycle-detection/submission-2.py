# Linked List Cycle Detection - Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while slow and fast:
            fast = fast.next.next if fast.next else None
            slow = slow.next

            if fast and slow and fast == slow:
                return True

        return False
