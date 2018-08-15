'''
make a common_prefix variable equal to an empty string
get the length of the list, call this list_len
find minimum length of all strings in the list
    how?
    set minimum = len first element
    check if length of each item is less than minimum
    if so set minimum at that value

while i is less than minimum length
compare first char of all elements in the list
if same
    store that char in common_prefix
    continue
if different
    exit loop
return common_prefix

edge cases:
    no list
    index errors
    empty string in list
    one string shorter than the rest
    all empty strings in list
    strings with double letters at beginning - aardvark, aaron
    all strings identical
    all strings different
    all strings same and all chars in strings same - bbbb,bbbb,bbbb,bbbb
    all but one: aaaab aaaac
    only one element in list
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        minimum = len(strs[0])

        for item in strs:
            if len(item) < minimum:
                minimum = len(item)

        for i in range(minimum - 2):
            for string in strs:
                if string[i] != string[i + 1]:
                    break

        index = i - 1
        if index == -1:
            return ''
        else:
            return strs[0][i]


