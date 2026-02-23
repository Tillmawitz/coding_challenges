"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:

    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""
# The "pythonic" choice, fastest as well by perhaps against the spirit of the question
class pythonicSolution:
    def reverseWords(self, s: str) -> str:
        full_str = s.strip().split()
        full_str.reverse()
        return " ".join(full_str)

# Assuming we cannot make extensive use of the built in methods, not as fast but more memory efficient
class anotherSolution:
    def reverseWords(self, s: str) -> str:
        final_string = ""
        start_ind = -1

        for index, char in enumerate(s):
            if char.isspace():
                if start_ind >= 0:
                    final_string = s[start_ind:index] + " " + final_string
                    start_ind = -1
                continue
            
            if start_ind < 0:
                start_ind = index
        
        if start_ind >= 0:
            final_string = s[start_ind:] + " " + final_string
            
        return final_string.strip()

# The provided "pythonic" solution
class morePythonicSolution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

# If using a language with mutable strings, you could do a variation of this to perform the operation in place
class inPlaceSolution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != " ":
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # converst string to char array
        # and trim spaces at the same time
        l = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # reverse each word
        self.reverse_each_word(l)

        return "".join(l)

# A solution using queues, similar to mine but likely more overhead
from collections import deque

class queueSolution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))

        return " ".join(d)