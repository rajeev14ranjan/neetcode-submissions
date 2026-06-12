# Merge K Sorted Linked Lists
# You are given an array of k linked lists lists, where each list is sorted in ascending order.

# Return the sorted linked list that is the result of merging all of the individual linked lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        currs = [c for c in lists if c]
        while any([True for c in currs if c]):
            min_idx = len(currs)
            min_val = math.inf
            for i, c in enumerate(currs):
                if not c:
                    continue

                if c.val < min_val:
                    min_idx = i
                    min_val = c.val

            # min_idx is the minimum index
            minc = currs[min_idx]
            curr.next = minc
            curr = minc
            currs[min_idx] = minc.next

        return dummy.next
