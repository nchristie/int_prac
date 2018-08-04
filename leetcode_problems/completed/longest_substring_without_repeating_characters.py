class Solution(object):
    #     def get_all_substrings(self, s, index_list_size):

    #         return substring_list

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # check s exists
        # if s:
        #     longest_substring = s[0]
        # else:
        #     return 0
        #
        # # check if s is already unique:
        # eliminate_char_list = []
        # for char in s:
        #     if s.count(char) != 1:
        #         if char not in eliminate_char_list:
        #             eliminate_char_list.append(char)
        # if eliminate_char_list == []:
        #     return len(s)
        #
        # # make substring list
        # substring_list = []
        # for i in range(len(s)):
        #     for j in range(len(s) + 1):
        #         substring = s[i:j]
        #         if substring not in substring_list:
        #             substring_list.append(substring)
        #
        # # check for repeated chars
        # eliminate_string_list = []
        # for string in substring_list:
        #     for char in string:
        #         if string.count(char) != 1:
        #             if string not in eliminate_string_list:
        #                 eliminate_string_list.append(string)
        #
        # # remove all the strings with repeats from main list
        # for string in eliminate_string_list:
        #     if string in substring_list:
        #         substring_list.remove(string)
        #
        # # check substring list for longest substring
        # for string in substring_list:
        #     if len(string) > len(longest_substring):
        #         longest_substring = string
        #
        # return len(longest_substring)

        # inputs : s, index_list_size

        if index_list_size < 1:
            return 0
        elif index_list_size == 1:
            return 1

        substring_start = 0
        substring_end = 1
        longest_substring = 1

        while substring_end+1 < index_list_size:
            if s[substring_end+1] not in s[substring_start:substring_end]:

'''
if next char doesn't exist in substring substring_end  = next_char 
else find location of char in substring
new substring_start is one after that first instance of char 
substring_end  = next_char
'''


my_string = 'abcabcdef'
'''
abcabcdef
...
a
ab
abc
abca !
bcab !
cabc !
abcd
abcde
abcdef
...
pwwkew
p
pw
pww!
wk
wke
wkew!
...
if no string
return 0
if string length one char then
substring_start = 0
substring_end = 1
longest_substring = len(substring)

loop >>
while next char < len full_string:
if next char doesn't exist in substring substring_end  = next_char 
else find location of char in substring
new substring_start is one after that first instance of char 
substring_end  = next_char

'''


x = Solution()
print(x.lengthOfLongestSubstring(my_string))



