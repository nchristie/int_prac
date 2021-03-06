'''

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        index_list_len = len(height) - 1

        i = 0
        j = index_list_len
        max_area = 0

        while j > i:

            smallest = min(height[i], height[j])

            dist = (j - i)
            area = smallest * dist
            max_area = area if area > max_area else max_area

            if smallest == height[i]:
                i += 1
            else:
                j -= 1

        return max_area

x = Solution()
print(x.maxArea([1,2,3,4,5]))
