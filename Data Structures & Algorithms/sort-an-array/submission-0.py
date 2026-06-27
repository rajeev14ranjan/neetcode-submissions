# Sort an Array
# You are given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
# **** Merge Sort *****

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int])-> List[int]:
            i, j = 0, 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            res.extend(left[i:])
            res.extend(right[j:])

            return res
        
        def merge_sort(arry: List[int]) -> List[int]:
            if len(arry) <= 1: return arry

            mid = len(arry) // 2
            left = merge_sort(arry[:mid])
            right = merge_sort(arry[mid:])

            return merge(left, right)

        return merge_sort(nums)