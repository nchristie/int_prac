'''
There are two sorted arrays nums1 and nums2 of 
size m and n respectively.

Find the median of the two sorted arrays. 
The overall run time complexity should be 
O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        full_array = nums1 + nums2
        length = len(full_array)
        if length %2 > 0:
            middle = (length / 2.0 - 0.5)
            return full_array[int(middle)]
        else:
            mid1 = length / 2
            mid2 = mid1+1
            return (mid1+mid2)/2

nums1 = [1, 3]
nums2 = [2]

nums1 = [1, 2]
nums2 = [3, 4]

nums1 = [1, 2]
nums2 = []
x = Solution()

print(x.findMedianSortedArrays(nums1, nums2))

