# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        We create a list of all the alphanumeric characters in the string, and then we compare that list
        to its reverse
        
        Args:
          s: the string to be checked
        
        Returns:
          The return value is a boolean value.
        """
        # Creating a list of all the alphanumeric characters in the string.
        s = [i for i in s.lower() if i.isalnum()]

        # Checking if the list is equal to its reverse.
        return s == s[::-1]
