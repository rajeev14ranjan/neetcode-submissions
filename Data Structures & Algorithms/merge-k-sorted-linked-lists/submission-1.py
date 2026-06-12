# Merge K Sorted Linked Lists
# You are given an array of k linked lists lists, where each list is sorted in ascending order.

# Return the sorted linked list that is the result of merging all of the individual linked lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# using *************** min heap ***************

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        heap = []
        # Push the head of each list into the heap
        # We include `i` (index) as a tie-breaker so Python doesn't try to compare ListNode objects directly
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
                
        while heap:
            # Pop the smallest node out of the heap - takes O(log k)
            val, i, minc = heapq.heappop(heap)
            
            curr.next = minc
            curr = minc
            
            # If this list has more nodes, push the next node into the heap
            if minc.next:
                heapq.heappush(heap, (minc.next.val, i, minc.next))
                
        return dummy.next