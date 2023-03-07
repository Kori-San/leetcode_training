# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        It checks if a number is a palindrome.
        
        Args:
          x: an integer
        
        Returns:
          The return value is a boolean value.
        """
        # The above code is checking if the number is positive and if the number is a palindrome.
        return x >= 0 and (str(x) == str(x)[::-1])
