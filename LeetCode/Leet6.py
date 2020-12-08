class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        lines = [''] * numRows
        count = 0
        direction = 1
        for c in s:
            lines[count] = lines[count] + c
            if count + direction > numRows - 1:
                adder = -1
            elif count + direction < 0:
                adder = 1
            count = count + direction
        return ''.join(lines)