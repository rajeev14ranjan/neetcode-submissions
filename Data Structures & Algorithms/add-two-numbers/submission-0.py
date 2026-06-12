# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1, d2 = l1, l2 # d1 and d2 are digit1 and digit2
        ans = ListNode()
        curr = ans
        reminder = 0

        while d1 or d2 or reminder:
            sum = (int(d1.val) if d1 else 0) + (int(d2.val) if d2 else 0) + reminder
            reminder = sum // 10
            curr.next = ListNode(sum % 10)
            
            curr = curr.next
            d1 = d1.next if d1 else None
            d2 = d2.next if d2 else None

        return ans.next
