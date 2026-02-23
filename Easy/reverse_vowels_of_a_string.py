"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
"""

class mySolution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left <= right:
            left_vowel = s_list[left] in vowels
            right_vowel = s_list[right] in vowels

            if left_vowel and right_vowel:
                s_list[left], s_list[right] = s_list[right], s_list[left]
            elif left_vowel:
                right -= 1
                continue
            elif right_vowel:
                left += 1
                continue

            left += 1
            right -= 1 

        return ''.join(s_list)

# No python solution provided, logic was same as mine