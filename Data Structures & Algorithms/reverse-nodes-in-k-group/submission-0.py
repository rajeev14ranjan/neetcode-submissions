# Reverse Nodes in K-Group
# You are given the head of a singly linked list head and a positive integer k.

# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

# Return the modified list after reversing the nodes in each group of k.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevgroup = dummy

        while True:
            kth = self.getKth(prevgroup, k)
            if not kth:
                break

            nextgroup = kth.next
            prev, curr = kth.next, prevgroup.next

            while curr != nextgroup:
                curr.next, prev, curr = prev, curr, curr.next

            prevgroup.next, prevgroup = kth, prevgroup.next

        return dummy.next

    def getKth(self, curr, c):
        while curr and c > 0:
            curr = curr.next
            c -= 1
        return curr
