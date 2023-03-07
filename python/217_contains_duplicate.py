# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        Sort the list, then check if any adjacent elements are equal
        
        Args:
          nums: the list of numbers
        
        Returns:
          A boolean value.
        """
        # Sorting the list in place.
        nums.sort()

        # Checking if any adjacent elements are equal.
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        # The default return value.
        return False
