"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= s.length
"""

# Standard sliding window solution
class mySolution:
    def maxVowels(self, s: str, k: int) -> int:
        start = end = 0
        largest_count = 0
        window_count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        while end < len(s):
            if s[end] in vowels:
                window_count += 1
            largest_count = max(largest_count, window_count)
            end += 1

            if end - start >= k:
                if s[start] in vowels:
                    window_count -= 1
                start += 1
        
        return largest_count

# My solution was algorithmically optimal, this is just a different way of doing the solution.
class compactSolution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Build the window of size k, count the number of vowels it contains.
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count
        
        # Slide the window to the right, focus on the added character and the
        # removed character and update "count". Record the largest "count".
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)
        
        return answer