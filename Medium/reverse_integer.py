"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:

    -231 <= x <= 231 - 1
"""

# While not optimal by any means, my solution was quick to write and works. Definitely not a "good" solution, but one that can be iterated on to get to the better, math based solutions. 
class mySolution:
    def reverse(self, x: int) -> int:
        s = ""
        if x < 0:
            s = "-"
            x = x * -1
        
        str_max = str(2 ** 31 - 1)
        str_min = str(2 ** 31)
        num_string = str(x)[::-1]

        if s == "-":
            if len(num_string) < len(str_min) or num_string <= str_min:
                return int(s + num_string)
            else:
                return 0
        else:
            if len(num_string) < len(str_max) or num_string <= str_max:
                return int(num_string)
            else:
                return 0

class optimalSolution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0
        return sign * rev