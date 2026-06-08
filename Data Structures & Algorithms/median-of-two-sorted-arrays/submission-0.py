# Median of Two Sorted Arrays
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in O(log(m+n)) time.
#  Hard because of required time complexity.
#  Easy with O(n)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        n = len(a) + len(b)

        if len(a) > len(b):
            a, b = b, a

        l, r = 0, len(a) - 1
        while True:  # since median is guranteed
            ma = (l + r) // 2
            mb = (n // 2) - ma - 2  # try it out, ma and mb are index.

            # reading elements on each side of ma and mb
            al = -math.inf if ma < 0 else a[ma]
            ar = math.inf if ma > len(a) - 2 else a[ma + 1]

            bl = -math.inf if mb < 0 else b[mb]
            br = math.inf if mb > len(b) - 2 else b[mb + 1]

            # see if this is valid partition
            if al <= br and bl <= ar:
                if n & 1:  # n is odd
                    return min(ar, br)
                else:
                    return (max(al, bl) + min(ar, br)) / 2
            elif al > br: # then this elm cannot be in 1st partation, so m needs to reduce.
                r = ma - 1
            else: # bl > ar -> The partion in a(ma) needs to increase
                l = ma + 1
