# Add Two Numbers
# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return ListNode(0)
        
        d1, d2 = l1, l2 # d1 and d2 are digit1 and digit2
        ans = ListNode()
        curr = ans
        overflow = 0

        while d1 or d2 or overflow:
            sum = (int(d1.val) if d1 else 0) + (int(d2.val) if d2 else 0) + overflow
            overflow = sum // 10
            curr.next = ListNode(sum % 10)
            
            curr = curr.next
            d1 = d1.next if d1 else None
            d2 = d2.next if d2 else None

        return ans.next
