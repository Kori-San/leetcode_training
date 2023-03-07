# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        It checks if two strings are anagrams.
        
        Args:
          s: the first string
          t: the type of the parameter
        
        Returns:
          A boolean value.
        """
        # Sort both of strings to see if they contain the same letters with the same amount
        # ie. sorted(bac)->abc == sorted(cab)->abc
        return sorted([i for i in s]) == sorted([j for j in t])
