# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Loop through the string, slicing it by a step of 'step' value, and check if the substring is
        longer than the longest substring
        
        Args:
          s: str
        
        Returns:
          The length of the longest substring without repeating characters.
        """
        # Special cases
        if len(s) == 0 or len(s) == 1:
            return len(s)

        long_sub = 0  # Count longest substring lenght
        step = 0

        while step < len(s):
            temp_list = []  # Temp list containing substrings

            # Looping through letters of s sliced by a step of 'step' value
            for letter in s[step::]:
                # Checking if the letter is already in the temp_list.
                if letter not in temp_list:
                    # If it is, then it breaks the loop.
                    temp_list.append(letter)
                # It breaks the loop if the letter is already in the temp_list.
                else:
                    break

            # Check if the new substring is longer than the longest
            if len(temp_list) > long_sub:
                long_sub = len(temp_list)

            # Increase step
            step += 1

        # Return length of longest substring
        return long_sub
