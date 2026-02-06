"""
Given an integer x, return true if x is a , and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?
"""
# simple moving pointers string solution
class initialSolution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        if len(num_string) == 0:
            return False

        start = 0
        end = len(num_string) - 1

        while start <= end:
            if num_string[start] != num_string[end]:
                return False
            start += 1
            end -= 1
        
        return True

# My solution to the follow up, construct the reverse as a number then compare equality
class followupSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        tmp = x

        while tmp > 0:
            digit = tmp % 10
            rev = rev * 10 + digit
            tmp = tmp // 10
        
        return rev == x

# Solution only reverses half the number then compares
class optimalSolution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        # When the length is an odd number, we can get rid of the middle digit by revertedNumber//10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == revertedNumber or x == revertedNumber // 10