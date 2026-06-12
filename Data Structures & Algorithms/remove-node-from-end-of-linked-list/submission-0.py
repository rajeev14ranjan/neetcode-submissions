# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front = head
        back = dummy

        c = 1
        while front:
            front = front.next
            c += 1

            if c > n+1:
                back = back.next
        
        # remove node
        back.next = back.next.next

        return dummy.next