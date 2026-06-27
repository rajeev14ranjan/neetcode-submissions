# Sort an Array
# You are given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
# **** Quick Sort *****
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:        
        def quick_sort(arry: List[int]) -> List[int]:
            if len(arry) <= 1: return arry
            
            # choose a random pivot point
            pivot = arry[random.randint(0, len(arry)-1)]
            left = [x for x in arry if x < pivot]
            middle = [x for x in arry if x == pivot]
            right = [x for x in arry if x > pivot]

            return quick_sort(left) + middle + quick_sort(right)

        return quick_sort(nums)