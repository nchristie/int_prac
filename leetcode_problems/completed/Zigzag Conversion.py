# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

'''

P   A   H   N
A P L S I I G
Y   I   R

P     H 
A    SI
Y  I  R
P L   I G   
A     N

rows = 3
middle = 1

rows = 4
middle = 2

rows = 5
middle = 3

rows = 6
middle = 4

'''


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row_dict = {}
        for i in range(1,numRows+1):
            row_dict[i]=''

        j = 0
        i = 1

        while j < len(s):
            while i < numRows:

                try:
                    row_dict[i]+=s[j]
                except:
                    pass

                i+=1
                j+=1

            while i > 1:

                try:
                    row_dict[i]+=s[j]
                except:
                    pass

                i-=1
                j+=1

        result = ''
        for i in range(1,numRows):
            result = result + row_dict[i]

        return(result)

s = 'PAYPALISHIRING'
x = Solution()
print(x.convert(s, 5))

