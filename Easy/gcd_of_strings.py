"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"

Output: ""

Example 4:

Input: str1 = "AAAAAB", str2 = "AAA"

Output: ""

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shorter = str1 if len(str1) <= len(str2) else str2
        longer = str1 if len(str1) > len(str2) else str2

        right = 1
        longest_ind = 0
        def divides(full_string: str, divisor: str) -> bool:
            repeats = len(full_string) // len(divisor)
            if divisor * repeats == full_string:
                return True
            else:
                return False

        while right <= len(shorter):
            if len(shorter) % right != 0:
                right += 1
                continue
            
            if divides(shorter, shorter[:right]) and divides(longer, shorter[:right]):
                longest_ind = right
            
            right += 1
        
        if longest_ind > 0:
            return shorter[:longest_ind]
        else:
            return ""

class cleanerSolution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            if len1 % k or len2 % k: 
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""

# If both strings are multiples of an identical segment, their concatenations must be the same
# The gcd string must then be of the same length as the gcd of the lengths of the two strings
class optimalSolution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]