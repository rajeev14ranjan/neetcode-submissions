# Reorder Linked List
# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:
# [0, 1, 2, 3, 4, 5, 6]
# Reorder the nodes of the linked list to be in the following order:
# [0, 6, 1, 5, 2, 4, 3]
# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
# [0, n-1, 1, n-2, 2, n-3, ...]
# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        last_slow = slow
        while fast and fast.next:
            fast = fast.next.next
            last_slow = slow
            slow = slow.next
        
        if slow == head: return

        # slow is at mid
        mid = slow
        last_slow.next = None  # cuttig the end of first list

        # reverse the second half
        prev = None
        curr = mid
        while curr:
            curr.next, curr, prev = prev, curr.next, curr

        mid = prev  # reversed second list

        # now merge them
        container = ListNode()  # container for holding
        curr = container
        p1 = head
        p2 = mid
        toggle = True
        while p1 and p2:
            if toggle:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next

            toggle = not toggle
            curr = curr.next

        curr.next = p1 or p2
        head = container.next

    # def pl(self, h):
    #     ans = []
    #     while h:
    #         ans.append(str(h.val))
    #         h = h.next
    #     print(" -> ".join(ans))
