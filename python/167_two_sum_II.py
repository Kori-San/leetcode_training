# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific
        target
        
        Args:
          numbers: an array of integers
          target: the target number

        Returns:
          Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2. 
        """
        # Iterating through the list of numbers.
        for i in range(len(numbers)):
            # Checking if the previous number is the same as the current number. If it is, it will skip
            # the current number.
            if numbers[i - 1] == numbers[i]:
                continue

            # Subtracting the target number from the current number.
            seeked = target - numbers[i]

           # Checking if the seeked number is in the list of numbers. If it is, it will replace the
           # current number with an "X" and return the index of the current number and the index of the
           # seeked number.
            if seeked in numbers[i + 1::]:
                numbers[i] = "X"
                return [i + 1, numbers.index(seeked) + 1]
