# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        I take the two arrays, combine them, sort them, and then return the median
        
        Args:
          nums1: [1, 2]
          nums2: [1, 2]
        
        Returns:
          The median of the two arrays.
        """

        # It's creating an empty array.
        all_nums = []

        # It's taking the array nums2 and adding each element to the array all_nums.
        for num in nums2:
            all_nums.append(num)

        # It's taking the array nums1 and adding each element to the array all_nums.
        for num in nums1:
            all_nums.append(num)

        # It's sorting the array all_nums.
        all_nums.sort()

        # It's taking the length of the array all_nums and dividing it by 2. It's then taking the middle
        # number of the array and assigning it to the variable middle_num.
        half = len(all_nums) / 2
        middle_num = all_nums[half]

        # It's checking if the length of the array all_nums is even. If it is, it's returning the average of
        # the middle number and the number before it. If it's not, it's returning the middle number.
        if len(all_nums) % 2 == 0:
            return ((middle_num + all_nums[half - 1]) / 2.0)
        else:
            return middle_num
