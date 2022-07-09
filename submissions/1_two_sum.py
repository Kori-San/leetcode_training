# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            seeked = target - nums[i]
            if seeked in nums[i + 1::]:
                nums[i] = "X"
                return [i, nums.index(seeked)]
