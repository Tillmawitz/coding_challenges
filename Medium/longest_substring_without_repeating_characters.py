"""
Given a string s, find the length of the longest without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""

class my_Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_chars = {}
        sub_str = ""
        longest_sub = 0

        for char in s:
            char_ind = sub_chars.get(char)
            if char_ind is not None:
                if len(sub_str) > longest_sub:
                    longest_sub = len(sub_str)
                
                next_ind = char_ind + 1
                if next_ind >= len(s):
                    break
                
                sub_str = sub_str[next_ind:]
                sub_chars = {sub_char: sub_idx for sub_idx, sub_char in enumerate(sub_str)}
            
            sub_chars[char] = len(sub_str)
            sub_str = sub_str + char
        
        if len(sub_str) > longest_sub:
            return len(sub_str)
        else:
            return longest_sub

# No need to do complicated hashmap/substring rebuild, indices act as pointers
# j - i + 1 is length of substring, i is starting index and j is ending index. No need to store actual substring
# mp stores index of letter + 1 to move starting index. Could store letter index and add 1 on retrieval for same result
class optimal_Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # charToNextIndex stores the index after current character
        charToNextIndex = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1

        return ans