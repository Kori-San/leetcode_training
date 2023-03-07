# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        It takes in a list of numbers and a target number and returns the indices of the two numbers that
        add up to the target.
        
        Args:
          nums: an array of integers
          target: the target number we're trying to find
        """
        # It's iterating through the list of numbers.
        for i in range(len(nums)):
            # It's subtracting the target number from the current number in the list.
            seeked = target - nums[i]

            # It's checking if the seeked number is in the list of numbers. If it is, it replaces the
            # current number with an X and returns the indices of the two numbers that add up to the
            # target.
            if seeked in nums[i + 1::]:
                nums[i] = "X"
                return [i, nums.index(seeked)]
