# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            if numbers[i - 1] == numbers[i]:
                continue
            seeked = target - numbers[i]
            if seeked in numbers[i + 1::]:
                numbers[i] = "X"
                return [i + 1, numbers.index(seeked) + 1]
