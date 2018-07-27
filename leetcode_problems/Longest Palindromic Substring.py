# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

def is_palindrome(substring):
    return substring == substring[::-1]


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if type(s) != basestring:
        #     raise Exception('No string to evaluate')
        # elif s.isEmpty():
        #     return ''
        # elif not s:
        #     raise Exception('No string to evaluate')

        longest_palindrome = s[0]
        length_of_longest_palindrome = 1

        for start_char in xrange(len(s)):
            for end_char in xrange(start_char, len(s) + 1):
                substring = s[start_char:end_char]
                # print(substring)
                if is_palindrome(substring):
                    if len(substring) > length_of_longest_palindrome:
                        longest_palindrome = substring
                        length_of_longest_palindrome = len(substring)

        return longest_palindrome


