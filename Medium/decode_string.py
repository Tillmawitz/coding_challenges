"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:

    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""

# Need to use a stack since the encodings can be nested, otherwise very straightforward
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                # Construct the encoded string
                tmp_string = stack.pop()
                while stack[-1] != "[":
                    tmp_string = stack.pop() + tmp_string
                # Remove the bracket
                stack.pop()
                # This will always be a number because the input is gaurunteed to be well formed
                k_str = stack.pop()
                while len(stack) > 0 and stack[-1].isnumeric():
                    k_str = stack.pop() + k_str
                k = int(k_str)
                tmp_string = tmp_string * k
                
                # Add the decoded string to the stack
                for tmp_char in tmp_string:
                    stack.append(tmp_char)
            else:
                stack.append(char)
        
        return "".join(stack)