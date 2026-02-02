"""
Zigzag meaning
string: "PAYPALISHIRING"
zigzag with numRows = 3:
P A H N
APLSIIG
Y I R
return: PAHNAPLSIIGYIR

Originally solved 2/2/26
"""

# O(numRows * n) in both space and time complexity
class mySolution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        zig_zag = [[""] * (len(s) // 2 + 1) for _ in range(numRows)]
        going_down = True
        row = 0
        column = 0
        final_string = ""

        for letter in s:
            zig_zag[row][column] = letter
            if going_down:
                row += 1
                if row >= numRows:
                    going_down = False
                    row = numRows - 2
                    column += 1
            else:
                row -= 1
                if row < 0:
                    going_down = True
                    row = 1
                else:
                    column += 1
        
        for row in zig_zag:
            final_string = final_string + "".join(row).strip(" ")
        
        return final_string

# Time O(n) space O(1)
# Section refers to each numRows x (numRows-1) matrix section of the zigzag
class optimal_Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = []
        n = len(s)
        chars_in_section = 2 * (numRows - 1)

        for curr_row in range(numRows):
            index = curr_row
            while index < n:
                answer.append(s[index])

                # If curr_row is not the first or last row,
                # then we have to add one more character of current section.
                if curr_row != 0 and curr_row != numRows - 1:
                    chars_in_between = chars_in_section - 2 * curr_row
                    second_index = index + chars_in_between

                    if second_index < n:
                        answer.append(s[second_index])
                # Jump to same row's first character of next section.
                index += chars_in_section

        return "".join(answer)